#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 下午2:37
# @Author  : pengyuan.li
# @Site    : 
# @File    : 03targetEncoding.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, train_test_split

# train -> training dataframe
# test -> test dataframe
data = pd.read_csv("./testPdf202110.csv")
feature = 'col_4'
target = "col_55"
X = data[feature]
y = data['col_55']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_test.shape, y_test.shape)
train = pd.concat([X_train, y_train], axis=1)
test = pd.concat([X_test, y_test], axis=1)


# n_folds = 20
# n_inner_folds = 10
# likelihood_encoded = pd.Series()
# likelihood_coding_map = {}
#
# oof_default_mean = train[target].mean()  # global prior mean
# kf = KFold(n_splits=n_folds, shuffle=True)
# oof_mean_cv = pd.DataFrame()
# split = 0
#
# for infold, oof in kf.split(train[feature]):
#     print('==============level 1 encoding..., fold %s ============' % split)
#     inner_kf = KFold(n_splits=n_inner_folds, shuffle=True)
#     inner_oof_default_mean = train.iloc[infold][target].mean()
#     inner_split = 0
#     inner_oof_mean_cv = pd.DataFrame()
#
#     likelihood_encoded_cv = pd.Series()
#     for inner_infold, inner_oof in inner_kf.split(train.iloc[infold]):
#         print('==============level 2 encoding..., inner fold %s ============' % inner_split)
#         # inner out of fold mean
#         oof_mean = train.iloc[inner_infold].groupby(by=feature)[target].mean()
#         # assign oof_mean to the infold
#         print(oof_mean.index)
#         train.iloc[infold].apply(
#             lambda x: oof_mean[x[feature]]
#             if x[feature] in oof_mean.index
#             else inner_oof_default_mean, axis=1)
#
#
#         likelihood_encoded_cv.append(train.iloc[infold].apply(
#             lambda x: oof_mean[x[feature]]
#             if x[feature] in oof_mean.index
#             else inner_oof_default_mean, axis=1))
#         inner_oof_mean_cv = inner_oof_mean_cv.join(pd.DataFrame(oof_mean), rsuffix=inner_split, how='outer')
#         inner_oof_mean_cv.fillna(inner_oof_default_mean, inplace=True)
#         inner_split += 1
#
#     oof_mean_cv = oof_mean_cv.join(pd.DataFrame(inner_oof_mean_cv), rsuffix=split, how='outer')
#     oof_mean_cv.fillna(value=oof_default_mean, inplace=True)
#     split += 1
#     print('============final mapping...===========')
#     likelihood_encoded = likelihood_encoded.append(train.iloc[oof].apply(
#         lambda x: np.mean(inner_oof_mean_cv.loc[x[feature]].values)
#         if x[feature] in inner_oof_mean_cv.index
#         else oof_default_mean, axis=1))
#
# ######################################### map into test dataframe
# train[feature] = likelihood_encoded
# likelihood_coding_mapping = oof_mean_cv.mean(axis=1)
# default_coding = oof_default_mean
#
# likelihood_coding_map[feature] = (likelihood_coding_mapping, default_coding)
# mapping, default_mean = likelihood_coding_map[feature]
# test[feature] = test.apply(lambda x: mapping[x[feature]]
# if x[feature] in mapping
# else default_mean, axis=1)

def add_noise(series, noise_level):
    return series * (1 + noise_level * np.random.randn(len(series)))


def target_encode(trn_series=None,
                  tst_series=None,
                  target=None,
                  min_samples_leaf=1,
                  smoothing=1,
                  noise_level=0):
    """
    Smoothing is computed like in the following paper by Daniele Micci-Barreca
    https://kaggle2.blob.core.windows.net/forum-message-attachments/225952/7441/high%20cardinality%20categoricals.pdf
    trn_series : training categorical feature as a pd.Series
    tst_series : test categorical feature as a pd.Series
    target : target data as a pd.Series
    min_samples_leaf (int) : minimum samples to take category average into account
    smoothing (int) : smoothing effect to balance categorical average vs prior
    """
    assert len(trn_series) == len(target)
    assert trn_series.name == tst_series.name
    temp = pd.concat([trn_series, target], axis=1)
    # Compute target mean
    averages = temp.groupby(by=trn_series.name)[target.name].agg(["mean", "count"])
    # Compute smoothing
    smoothing = 1 / (1 + np.exp(-(averages["count"] - min_samples_leaf) / smoothing))
    # Apply average function to all target data
    prior = target.mean()
    # The bigger the count the less full_avg is taken into account
    averages[target.name] = prior * (1 - smoothing) + averages["mean"] * smoothing
    averages.drop(["mean", "count"], axis=1, inplace=True)
    # Apply averages to trn and tst series
    ft_trn_series = pd.merge(
        trn_series.to_frame(trn_series.name),
        averages.reset_index().rename(columns={'index': target.name, target.name: 'average'}),
        on=trn_series.name,
        how='left')['average'].rename(trn_series.name + '_mean').fillna(prior)
    # pd.merge does not keep the index so restore it
    ft_trn_series.index = trn_series.index
    ft_tst_series = pd.merge(
        tst_series.to_frame(tst_series.name),
        averages.reset_index().rename(columns={'index': target.name, target.name: 'average'}),
        on=tst_series.name,
        how='left')['average'].rename(trn_series.name + '_mean').fillna(prior)
    # pd.merge does not keep the index so restore it
    ft_tst_series.index = tst_series.index
    return add_noise(ft_trn_series, noise_level), add_noise(ft_tst_series, noise_level)


trn, sub = target_encode(train[feature],
                         test[feature],
                         target=train[target],
                         min_samples_leaf=100,
                         smoothing=10,
                         noise_level=0.01)
print(trn.head(10))
