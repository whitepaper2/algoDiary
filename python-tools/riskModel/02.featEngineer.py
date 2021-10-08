# !/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

dfp = pd.read_csv('./features/dfp_features1.csv')

dfp['事件发生时间戳'] = dfp['事件发生时间'].apply(lambda x: float(x) / 1000)

dfp['事件发生时间'] = dfp.事件发生时间戳.apply(lambda x: str(pd.to_datetime(int(x), unit='s')))


def minutes_day(x):
    x = int(x[11:13]) * 60 + int(x[14:16])
    return x


def hours_day(x):
    x = int(x[11:13])
    return x


dfp['minutes_day'] = dfp.loc[:, '事件发生时间'].apply(minutes_day)
dfp['hours_day'] = dfp.loc[:, '事件发生时间'].apply(hours_day)

dfp = dfp.sort_values('事件发生时间戳', ascending=True)
dfp['事件发生时间'] = pd.to_datetime(dfp['事件发生时间'], format="%Y-%m-%d %H:%M:%S")
dfp = dfp.reset_index()

dfp_features = dfp.copy()


# ４．衍生特征用到的函数
def cat_series_to_int(series):
    encoder = LabelEncoder()
    encoder.fit(series)
    mapper = dict(zip(encoder.classes_, range(len(series))))
    series_encoded = encoder.transform(series)
    return series_encoded, mapper


def merge_rolling_fea(df, name, fea):
    join_cols = list(fea.index.names)
    fea.name = name
    fea = fea.reset_index()
    df_ = df.merge(fea, on=join_cols, how='left')
    return df_


###################################订单总金额##########################################
# 支持 天 为单位，计算均值、方差
def get_day_money_feas(df_, money_cols=['订单总金额'], id_cols=['用户电子邮箱'], days_before=7):
    prefix = 'f金额特征_{}_过去{}天___'.format('_'.join(id_cols), days_before)
    print(prefix)
    df = df_[id_cols + ['事件发生时间'] + money_cols].copy()
    gdf = df.groupby(id_cols, sort=False)
    wdf = gdf.rolling(window='{}d'.format(days_before), on='事件发生时间', min_periods=1)
    for mcol in money_cols:
        df = merge_rolling_fea(df, prefix + '{}mean'.format(mcol), wdf[mcol].mean())
        df = merge_rolling_fea(df, prefix + '{}std'.format(mcol), wdf[mcol].std())
    df = df.fillna(0)
    return df[[col for col in df.columns if col.startswith(prefix)]]


# 支持 小时 为单位，计算总和
def get_hour_money_feas(df_, money_cols=['订单总金额'], id_cols=['用户电子邮箱'], hours_before=24 * 7):
    prefix = 'f金额特征_{}_过去{}小时___'.format('_'.join(id_cols), hours_before)
    print(prefix)
    df = df_[id_cols + ['事件发生时间'] + money_cols].copy()
    gdf = df.groupby(id_cols, sort=False)
    wdf = gdf.rolling(window='{}h'.format(hours_before), on='事件发生时间', min_periods=1)
    for mcol in money_cols:
        df = merge_rolling_fea(df, prefix + '{}sum'.format(mcol), wdf[mcol].sum())
    df = df.fillna(0)
    return df[[col for col in df.columns if col.startswith(prefix)]]


#################################交易频率########################################    

def get_frequency_feas(df_, id_cols=['用户电子邮箱'], days_before=7):
    prefix = 'f频率特征_{}_过去{}天___'.format('_'.join(id_cols), days_before)
    print(prefix)
    df = df_[id_cols + ['事件发生时间']].copy()
    df['n'] = 1
    df[prefix + '本次交易与上次的时间差'] = df.groupby(id_cols, sort=False)['事件发生时间'].diff().dt.seconds.values
    wdf = df.groupby(id_cols, sort=False).rolling(window='{}d'.format(days_before), on='事件发生时间', min_periods=1)
    df = merge_rolling_fea(df, prefix + '交易次数', wdf['n'].count())
    df = merge_rolling_fea(df, prefix + '交易时间差mean', wdf[prefix + '本次交易与上次的时间差'].mean())
    df = merge_rolling_fea(df, prefix + '交易时间差std', wdf[prefix + '本次交易与上次的时间差'].std())
    df = df.fillna(0)
    return df[[col for col in df.columns if col.startswith(prefix)]]


# 计算与上一笔记录的相似程度
import math


def isEqual(difftime, curstr, prefixstr, dayslimit):
    curstr = str(curstr).lower()
    prefixstr = str(prefixstr).lower()
    if math.isnan(difftime) or (difftime < dayslimit and curstr == prefixstr):
        return 1
    else:
        return 0


#################################同一个ｉｄ，对应不同的账户数。同一个收货地址过去７天有多少个客户########################################
def get_multi_account_feas(df_, account_cols=['客户姓名'], id_cols=['用户电子邮箱'], days_before=90):
    prefix = 'f多号特征_{}_过去{}天___'.format('_'.join(id_cols), days_before)
    print(prefix)
    df = df_[id_cols + ['事件发生时间'] + account_cols].copy()

    gdf = df.groupby(id_cols, sort=False)
    for acol in account_cols:
        df[acol + '_last_time'] = gdf[acol].shift(1).values
        df['事件发生时间_last_time'] = gdf['事件发生时间'].shift(1).values
        df['time_diff'] = df['事件发生时间'] - df['事件发生时间_last_time']
        df[prefix + '{}是否与上次相同'.format(acol)] = df.apply(
            lambda x: isEqual(x['time_diff'].days, x[acol], x[acol + '_last_time'], days_before), axis=1)

    df = df.fillna(-1)
    return df[[col for col in df.columns if col.startswith(prefix)]]


# 支持 天 为单位，计算总和
def get_day_multi_account_feas(df_, account_cols=['客户姓名'], id_cols=['用户电子邮箱'], days_before=7):
    prefix = 'f多号特征_{}_过去{}天___'.format('_'.join(id_cols), days_before)
    print(prefix)
    df = df_[id_cols + ['事件发生时间'] + account_cols].copy()
    for acol in account_cols:
        df[acol] = cat_series_to_int(df[acol].astype(str))[0]

    wdf = df.groupby(id_cols, sort=False).rolling(window='{}d'.format(days_before), on='事件发生时间', min_periods=1)
    for acol in account_cols:
        df = merge_rolling_fea(df, prefix + '{}_nunique'.format(acol), wdf[acol].apply(lambda x: len(np.unique(x))))

    df = df.fillna(0)
    return df[[col for col in df.columns if col.startswith(prefix)]]


# 支持 小时 为单位，计算总和
def get_hour_multi_account_feas(df_, account_cols=['客户姓名'], id_cols=['用户电子邮箱'], hours_before=2):
    prefix = 'f多号特征_{}_过去{}小时___'.format('_'.join(id_cols), hours_before)
    print(prefix)
    df = df_[id_cols + ['事件发生时间'] + account_cols].copy()
    for acol in account_cols:
        df[acol] = cat_series_to_int(df[acol].astype(str))[0]

    wdf = df.groupby(id_cols, sort=False).rolling(window='{}h'.format(hours_before), on='事件发生时间', min_periods=1)
    for acol in account_cols:
        df = merge_rolling_fea(df, prefix + '{}_nunique'.format(acol), wdf[acol].apply(lambda x: len(np.unique(x))))

    df = df.fillna(0)
    return df[[col for col in df.columns if col.startswith(prefix)]]


################################### 1.订单总金额
money_feas = get_money_feas(dfp, ['订单总金额'], days_before=1)
dfp_features[money_feas.columns.tolist()] = money_feas  # 17min
del money_feas

money_feas = get_day_money_feas(dfp, ['订单总金额', '物流费用金额'], days_before=7)
dfp_features[money_feas.columns.tolist()] = money_feas  # 17min
del money_feas
money_feas = get_day_money_feas(dfp, ['订单总金额', '物流费用金额'], days_before=30)
dfp_features[money_feas.columns.tolist()] = money_feas  # 17min
del money_feas

total_money_feas = get_hour_money_feas(dfp, ['订单总金额', '物流费用金额'], hours_before=24)
dfp_features[total_money_feas.columns.tolist()] = total_money_feas  # 6min
del total_money_feas
total_money_feas = get_hour_money_feas(dfp, ['订单总金额', '物流费用金额'], hours_before=2)
dfp_features[total_money_feas.columns.tolist()] = total_money_feas  # 6min
del total_money_feas

################################# 2.交易频率
freq_feas = get_frequency_feas(dfp, id_cols=['用户电子邮箱'], days_before=1)
dfp_features[freq_feas.columns.tolist()] = freq_feas  # 10min
del freq_feas
freq_feas = get_frequency_feas(dfp, id_cols=['用户电子邮箱'], days_before=7)
dfp_features[freq_feas.columns.tolist()] = freq_feas  # 10min
del freq_feas
freq_feas = get_frequency_feas(dfp, id_cols=['用户电子邮箱'], days_before=30)
dfp_features[freq_feas.columns.tolist()] = freq_feas  # 40min
del freq_feas

multi_account_feas = get_multi_account_feas(dfp,
                                            ['客户姓名', '手机号码', '银行卡号', '来源IP', '设备ID', '收货州', '收货城市', '收货地址', '收货地址邮编',
                                             '收货国家'], id_cols=['用户电子邮箱'], days_before=90)
dfp_features[multi_account_feas.columns.tolist()] = multi_account_feas  # 20min
del multi_account_feas

################################　３.同一个id，对应不同的账户数
multi_account_feas = get_day_multi_account_feas(dfp,
                                                ['客户姓名', '手机号码', '来源IP', '收货地址', '设备ID', 'IP地区码', '银行卡号', '卡bin国家英文简码'],
                                                id_cols=['用户电子邮箱'], days_before=7)
dfp_features[multi_account_feas.columns.tolist()] = multi_account_feas  # 20min
del multi_account_feas

multi_account_feas = get_day_multi_account_feas(dfp,
                                                ['客户姓名', '手机号码', '来源IP', '收货地址', '设备ID', 'IP地区码', '银行卡号', '卡bin国家英文简码'],
                                                id_cols=['用户电子邮箱'], days_before=3)
dfp_features[multi_account_feas.columns.tolist()] = multi_account_feas  # 20min
del multi_account_feas

multi_account_feas = get_day_multi_account_feas(dfp, ['客户姓名', '用户电子邮箱', '银行卡号'], id_cols=['手机号码'], days_before=7)
dfp_features[multi_account_feas.columns.tolist()] = multi_account_feas  # 12min
del multi_account_feas

multi_account_feas = get_day_multi_account_feas(dfp, ['用户电子邮箱', '银行卡号', '收货地址'], id_cols=['客户姓名'], days_before=7)
dfp_features[multi_account_feas.columns.tolist()] = multi_account_feas  # 20min
del multi_account_feas

multi_account_feas = get_day_multi_account_feas(dfp,
                                                ['客户姓名', '手机号码', '来源IP', '收货地址', '设备ID', 'IP地区码', '银行卡号', '卡bin国家英文简码'],
                                                id_cols=['用户电子邮箱'], days_before=30)
dfp_features[multi_account_feas.columns.tolist()] = multi_account_feas  # 20min
del multi_account_feas

multi_account_feas = get_day_multi_account_feas(dfp, ['客户姓名', '用户电子邮箱', '银行卡号'], id_cols=['手机号码'], days_before=30)
dfp_features[multi_account_feas.columns.tolist()] = multi_account_feas  # 12min
del multi_account_feas

multi_account_feas = get_day_multi_account_feas(dfp, ['用户电子邮箱', '银行卡号', '收货地址'], id_cols=['客户姓名'], days_before=30)
dfp_features[multi_account_feas.columns.tolist()] = multi_account_feas  # 20min
del multi_account_feas

multi_account_feas = get_hour_multi_account_feas(dfp, ['银行卡号', '设备ID', '客户姓名', '手机号码', '收货地址'], id_cols=['用户电子邮箱'],
                                                 hours_before=2)
dfp_features[multi_account_feas.columns.tolist()] = multi_account_feas  # 20min
del multi_account_feas

dfp_features.to_csv("./features/dfp_features2.csv", index=None)

dfp_features['物流金额占总金额比例'] = dfp['物流费用金额'] / (dfp['订单总金额'] + 0.0001)
dfp_features['订单单价'] = dfp['订单总金额'] / (dfp['订单商品数量'] + 0.0001)
dfp_features.loc[:, 'binTotalMoney'] = pd.cut(dfp['订单总金额'], bins=[float('-inf'), 50, 180, 500, float('inf')],
                                              labels=[1, 2, 3, 4])
dfp_features.loc[:, 'binFeeMoney'] = pd.cut(dfp['物流费用金额'], bins=[float('-inf'), 7, 20, 40, float('inf')],
                                            labels=[1, 2, 3, 4])
dfp_features['IP归属地和真实地址是否一致__国家'] = (dfp['IP地区码'] == dfp['真实IP归属地简码']).astype(np.int8)
dfp_features['IP归属地和真实地址是否一致__省份'] = (dfp['IP归属地省份'] == dfp['真实IP归属地省份']).astype(np.int8)
dfp_features['IP归属地和真实地址是否一致__城市'] = (dfp['IP归属地城市'] == dfp['真实IP归属地城市']).astype(np.int8)
dfp_features['IP归属地和卡bin国家是否一致'] = (dfp['IP地区码'] == dfp['卡bin国家英文简码']).astype(np.int8)
dfp_features['IP归属地和收货国家是否一致'] = (dfp['IP地区码'] == dfp['收货国家']).astype(np.int8)
dfp_features['是否使用COUPON=True'] = dfp['是否使用COUPON'].astype(str).apply(lambda x: 1 if x == "True" else 0)
dfp_features['用户电子邮箱后缀'] = dfp.用户电子邮箱.str.split('@', expand=True).iloc[:, 1]

# 国家风险特征
risk_dict = {"AL": "阿尔及利亚", "BR": "巴西", "CL": "智利", "CO": "哥伦比亚", "EG": "埃及", "IN": "印度", "MA": "摩洛哥", "MX": "墨西哥",
             "PE": "秘鲁", "RU": "俄罗斯", "ZA": "南非", "UA": "乌克兰", "VE": "委内瑞拉", "ID": "印度尼西亚", "PK": "巴基斯坦", "PH": "菲律宾"}
l = list(risk_dict.keys())
dfp_features['highRiskCountry'] = dfp.收货国家.apply(lambda x: 1 if x in l else 0)

sparse_features = ['收货国家', '收货州', '收货地址邮编', '卡bin国家英文简码', '支付方式', '交易币种', 'IP地区码', '用户电子邮箱后缀']
for feat in sparse_features:
    dfp_features[feat] = dfp_features[feat].astype(str)

train_inds = dfp_features.index[
    (dfp_features.事件发生时间 >= '2021-05-01 00:00:00') & (dfp_features.事件发生时间 < '2021-07-30 00:00:00')]
test_inds = dfp_features.index[
    (dfp_features.事件发生时间 >= '2021-07-30 00:00:00') & (dfp_features.事件发生时间 < '2021-08-20 00:00:00')]

train_pdf = dfp_features.iloc[train_inds, :]
test_pdf = dfp_features.iloc[test_inds, :]

# Convert categorical features to int type
# 空值nan,变为最大值；未出现，变为0
encoder_map = {}


def conv_cat(df, cols, train=True):
    if train:
        enc = OrdinalEncoder()
        enc.fit(df[cols])
        res = enc._transform(df[cols], handle_unknown='ignore')[0]
        encoder_map['cat_cols'] = enc
    else:
        enc = encoder_map['cat_cols']
        res = enc._transform(df[cols], handle_unknown='ignore')[0]
    dfc = df.copy()
    dfc.loc[:, cols] = res
    return dfc


sparseDict = {}
categories = encoder_map['cat_cols'].categories_
for i, feat in enumerate(sparse_features):
    sparseDict[feat] = {x: y for x, y in zip(categories[i], range(len(categories[i])))}

joblib.dump(sparseDict, './params/feas_count_mapper.m')
encodeTrainPdf = conv_cat(train_pdf, sparse_features, True)
encodeTestPdf = conv_cat(test_pdf, sparse_features, False)
encodeTrainPdf.to_csv("./features/dfp_features3_train.csv", index=None)
encodeTestPdf.to_csv("./features/dfp_features3_test.csv", index=None)
