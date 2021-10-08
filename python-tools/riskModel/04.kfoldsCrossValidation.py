#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gc

import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import TimeSeriesSplit

dfp_features = pd.read_csv("./features/dfp_features3_train.csv")
testModelPdf = pd.read_csv("./features/dfp_features3_test.csv")
select_cols = ['label', '事件发生时间', '风控决策结果',
               'hours_day',
               'f金额特征_用户电子邮箱_过去7天___订单总金额mean',
               'f金额特征_用户电子邮箱_过去7天___订单总金额std',
               'f金额特征_用户电子邮箱_过去7天___物流费用金额mean',
               'f金额特征_用户电子邮箱_过去7天___物流费用金额std',
               'f金额特征_用户电子邮箱_过去30天___订单总金额mean',
               'f金额特征_用户电子邮箱_过去30天___订单总金额std',
               'f金额特征_用户电子邮箱_过去30天___物流费用金额mean',
               'f金额特征_用户电子邮箱_过去30天___物流费用金额std',
               'f金额特征_用户电子邮箱_过去24小时___订单总金额sum',
               'f金额特征_用户电子邮箱_过去24小时___物流费用金额sum',
               'f金额特征_用户电子邮箱_过去2小时___订单总金额sum',
               'f金额特征_用户电子邮箱_过去2小时___物流费用金额sum',
               'f频率特征_用户电子邮箱_过去1天___本次交易与上次的时间差',
               'f频率特征_用户电子邮箱_过去1天___交易次数',
               'f频率特征_用户电子邮箱_过去1天___交易时间差mean',
               'f频率特征_用户电子邮箱_过去1天___交易时间差std',
               'f频率特征_用户电子邮箱_过去7天___本次交易与上次的时间差',
               'f频率特征_用户电子邮箱_过去7天___交易次数',
               'f频率特征_用户电子邮箱_过去7天___交易时间差mean',
               'f频率特征_用户电子邮箱_过去7天___交易时间差std',
               'f频率特征_用户电子邮箱_过去30天___本次交易与上次的时间差',
               'f频率特征_用户电子邮箱_过去30天___交易次数',
               'f频率特征_用户电子邮箱_过去30天___交易时间差mean',
               'f频率特征_用户电子邮箱_过去30天___交易时间差std',
               'f频率特征_设备ID_过去1天___交易次数',
               'f多号特征_用户电子邮箱_过去90天___客户姓名是否与上次相同',
               'f多号特征_用户电子邮箱_过去90天___手机号码是否与上次相同',
               'f多号特征_用户电子邮箱_过去90天___银行卡号是否与上次相同',
               'f多号特征_用户电子邮箱_过去90天___来源IP是否与上次相同',
               'f多号特征_用户电子邮箱_过去90天___设备ID是否与上次相同',
               'f多号特征_用户电子邮箱_过去90天___收货州是否与上次相同',
               'f多号特征_用户电子邮箱_过去90天___收货城市是否与上次相同',
               'f多号特征_用户电子邮箱_过去90天___收货地址是否与上次相同',
               'f多号特征_用户电子邮箱_过去90天___收货地址邮编是否与上次相同',
               'f多号特征_用户电子邮箱_过去90天___收货国家是否与上次相同',
               'f多号特征_用户电子邮箱_过去1天___客户姓名_nunique',
               'f多号特征_用户电子邮箱_过去1天___手机号码_nunique',
               'f多号特征_用户电子邮箱_过去1天___来源IP_nunique',
               'f多号特征_用户电子邮箱_过去1天___收货地址_nunique',
               'f多号特征_用户电子邮箱_过去1天___设备ID_nunique',
               'f多号特征_用户电子邮箱_过去1天___IP地区码_nunique',
               'f多号特征_用户电子邮箱_过去1天___银行卡号_nunique',
               'f多号特征_用户电子邮箱_过去1天___卡bin国家英文简码_nunique',
               'f多号特征_设备ID_过去1天___用户电子邮箱_nunique',
               'f多号特征_设备ID_过去1天___IP地区码_nunique',
               'f多号特征_设备ID_过去1天___银行卡号_nunique',
               'f多号特征_设备ID_过去1天___卡bin国家英文简码_nunique',
               'f多号特征_收货地址_过去1天___用户电子邮箱_nunique',
               'f多号特征_收货地址_过去1天___银行卡号_nunique',
               'f多号特征_收货地址_过去1天___卡bin国家英文简码_nunique',
               'f多号特征_用户电子邮箱_过去7天___客户姓名_nunique',
               'f多号特征_用户电子邮箱_过去7天___手机号码_nunique',
               'f多号特征_用户电子邮箱_过去7天___来源IP_nunique',
               'f多号特征_用户电子邮箱_过去7天___收货地址_nunique',
               'f多号特征_用户电子邮箱_过去7天___设备ID_nunique',
               'f多号特征_用户电子邮箱_过去7天___IP地区码_nunique',
               'f多号特征_用户电子邮箱_过去7天___银行卡号_nunique',
               'f多号特征_用户电子邮箱_过去7天___卡bin国家英文简码_nunique',
               'f多号特征_用户电子邮箱_过去3天___客户姓名_nunique',
               'f多号特征_用户电子邮箱_过去3天___手机号码_nunique',
               'f多号特征_用户电子邮箱_过去3天___来源IP_nunique',
               'f多号特征_用户电子邮箱_过去3天___收货地址_nunique',
               'f多号特征_用户电子邮箱_过去3天___设备ID_nunique',
               'f多号特征_用户电子邮箱_过去3天___IP地区码_nunique',
               'f多号特征_用户电子邮箱_过去3天___银行卡号_nunique',
               'f多号特征_用户电子邮箱_过去3天___卡bin国家英文简码_nunique',
               'f多号特征_手机号码_过去7天___客户姓名_nunique',
               'f多号特征_手机号码_过去7天___用户电子邮箱_nunique',
               'f多号特征_手机号码_过去7天___银行卡号_nunique',
               'f多号特征_客户姓名_过去7天___用户电子邮箱_nunique',
               'f多号特征_客户姓名_过去7天___银行卡号_nunique',
               'f多号特征_客户姓名_过去7天___收货地址_nunique',
               'f多号特征_用户电子邮箱_过去30天___客户姓名_nunique',
               'f多号特征_用户电子邮箱_过去30天___手机号码_nunique',
               'f多号特征_用户电子邮箱_过去30天___来源IP_nunique',
               'f多号特征_用户电子邮箱_过去30天___收货地址_nunique',
               'f多号特征_用户电子邮箱_过去30天___设备ID_nunique',
               'f多号特征_用户电子邮箱_过去30天___IP地区码_nunique',
               'f多号特征_用户电子邮箱_过去30天___银行卡号_nunique',
               'f多号特征_用户电子邮箱_过去30天___卡bin国家英文简码_nunique',
               'f多号特征_手机号码_过去30天___客户姓名_nunique',
               'f多号特征_手机号码_过去30天___用户电子邮箱_nunique',
               'f多号特征_手机号码_过去30天___银行卡号_nunique',
               'f多号特征_客户姓名_过去30天___用户电子邮箱_nunique',
               'f多号特征_客户姓名_过去30天___银行卡号_nunique',
               'f多号特征_客户姓名_过去30天___收货地址_nunique',
               'f多号特征_用户电子邮箱_过去2小时___银行卡号_nunique',
               'f多号特征_用户电子邮箱_过去2小时___设备ID_nunique',
               'f多号特征_用户电子邮箱_过去2小时___客户姓名_nunique',
               'f多号特征_用户电子邮箱_过去2小时___手机号码_nunique',
               'f多号特征_用户电子邮箱_过去2小时___收货地址_nunique',
               '物流金额占总金额比例',
               '订单单价',
               'binTotalMoney',
               'binFeeMoney',
               'IP归属地和真实地址是否一致__国家',
               'IP归属地和真实地址是否一致__省份',
               'IP归属地和真实地址是否一致__城市',
               'IP归属地和卡bin国家是否一致',
               'IP归属地和收货国家是否一致',
               '是否使用COUPON=True',
               'highRiskCountry',
               '收货国家', '收货州', '收货地址邮编', '卡bin国家英文简码', '支付方式', '交易币种', 'IP地区码', '用户电子邮箱后缀']

model_data = dfp_features[select_cols]
trainPdf = model_data[model_data.label != -1]
train_data = trainPdf.drop(['label', '风控决策结果', '事件发生时间'], axis=1)
train_label = trainPdf.label

test_pdf = testModelPdf[select_cols]
test_pdf = test_pdf[test_pdf.label != -1]
test_x = test_pdf.drop(['label', '风控决策结果', '事件发生时间'], axis=1)
test_y = test_pdf.label
test_data = test_x.copy()
test_label = test_y.copy()

bestIters = []
validf1 = []
testf1 = []
validauc = []
testauc = []


def f1(p, r):
    return round(2 * p * r / (p + r), 3)


skf = TimeSeriesSplit(n_splits=5)  # 五折交叉验证
for index, (train_index, valid_index) in enumerate(skf.split(train_data, train_label)):  # 将数据五折分割
    train_x, valid_x, train_y, valid_y = train_data.iloc[train_index], train_data.iloc[valid_index], train_label.iloc[
        train_index], train_label.iloc[valid_index]
    cbt_model = CatBoostClassifier(iterations=500, learning_rate=0.06, loss_function='Logloss', l2_leaf_reg=5,
                                   max_depth=6, verbose=20, early_stopping_rounds=400)  # 设置模型参数，verbose表示每100个训练输出打印一次
    cbt_model.fit(train_x, train_y, eval_set=(valid_x, valid_y))  # 训练五折分割后的训练集
    bestIters.append(cbt_model.best_iteration_)
    gc.collect()  # 垃圾清理，内存清理
    valid_pred = cbt_model.predict_proba(valid_x)[:, 1]
    test_pred = cbt_model.predict_proba(test_data)[:, 1]
    validauc.append(roc_auc_score(valid_y, valid_pred))
    testauc.append(roc_auc_score(test_label, test_pred))
    threshold = 0.25
    table = pd.crosstab(valid_y, valid_pred >= threshold, rownames=['label'], colnames=['preds'])
    validf1.append(f1(table.iloc[1, 1] / table.iloc[:, 1].sum(), table.iloc[1, 1] / table.iloc[1, :].sum()))
    table = pd.crosstab(test_label, test_pred >= threshold, rownames=['label'], colnames=['preds'])
    testf1.append(f1(table.iloc[1, 1] / table.iloc[:, 1].sum(), table.iloc[1, 1] / table.iloc[1, :].sum()))

evalPdf = pd.DataFrame(
    {"bestIters": bestIters, "validauc": validauc, "testauc": testauc, "validf1": validf1, "testf1": testf1},
    index=["1fold", "2fold", "3fold", "4fold", "5fold"])
evalPdfT = evalPdf.T
evalPdfT['mean'] = evalPdfT.mean(axis=1)
evalPdfT['std'] = evalPdfT.std(axis=1)
print("\n" * 5)
print("-" * 20, "5folds cross validation's evaluation", "-" * 20)
print(evalPdfT)
