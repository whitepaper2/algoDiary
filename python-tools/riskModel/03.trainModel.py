#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 下午5:36
# @Author  : pengyuan.li
# @Site    :
# @File    : 03.trainModel.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import precision_recall_curve, roc_auc_score

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
train_inds = model_data.index[
    (model_data.事件发生时间 >= '2021-05-01 00:00:00') & (model_data.事件发生时间 < '2021-07-10 00:00:00')]
valid_inds = model_data.index[
    (model_data.事件发生时间 >= '2021-07-10 00:00:00') & (model_data.事件发生时间 < '2021-07-30 00:00:00')]

train_pdf = model_data.iloc[train_inds, :]
train_pdf = train_pdf[train_pdf.label != -1]
valid_pdf = model_data.iloc[valid_inds, :]
valid_pdf = valid_pdf[valid_pdf.label != -1]

test_pdf = testModelPdf[select_cols]
test_pdf = test_pdf[test_pdf.label != -1]

train_x = train_pdf.drop(['label', '风控决策结果', '事件发生时间'], axis=1)
train_y = train_pdf.label
valid_x = valid_pdf.drop(['label', '风控决策结果', '事件发生时间'], axis=1)
valid_y = valid_pdf.label
test_x = test_pdf.drop(['label', '风控决策结果', '事件发生时间'], axis=1)
test_y = test_pdf.label

model = CatBoostClassifier(iterations=500,
                           depth=6,
                           learning_rate=0.06,
                           loss_function='Logloss',
                           l2_leaf_reg=5,
                           logging_level='Verbose', random_seed=2020)
model.fit(train_x, train_y, eval_set=(valid_x, valid_y), verbose=20)


# joblib.dump(model, './models/catboost0901v1.m')

def f1(p, r):
    print('precision:', round(p, 3), ' recall:', round(r, 3), ' f1:', round(2 * p * r / (p + r), 3))


pred_train = model.predict_proba(train_x)[:, 1]
train_auc = roc_auc_score(train_y, pred_train)
print('train auc:%s' % format(train_auc, '.2%'))
pred_valid = model.predict_proba(valid_x)[:, 1]
valid_auc = roc_auc_score(valid_y, pred_valid)
print('valid auc:%s' % format(valid_auc, '.2%'))
cat_probs01 = model.predict_proba(test_x)[:, 1]
test_auc = roc_auc_score(test_y, cat_probs01)
print('test auc:%s' % format(test_auc, '.2%'))

threshold = 0.25
table = pd.crosstab(valid_y, pred_valid >= threshold, rownames=['label'], colnames=['preds'])
print(table)
print('模型valid f1得分:')
f1(table.iloc[1, 1] / table.iloc[:, 1].sum(), table.iloc[1, 1] / table.iloc[1, :].sum())
origin_fraud = round((table.iloc[1, :].sum()) / (table.iloc[:, 0].sum() + table.iloc[:, 1].sum()), 4)
fraud = round(table.iloc[1, 0] / table.iloc[:, 0].sum(), 4)
reject = round((table.iloc[1, 1] + table.iloc[0, 1]) / (table.iloc[:, 0].sum() + table.iloc[:, 1].sum()), 4)

print('建模样本欺诈率：%s' % format(origin_fraud, '.2%'))
print('欺诈率：%s' % format(fraud, '.2%'))
print('拒绝率：%s' % format(reject, '.2%'))

print(min(cat_probs01), max(cat_probs01))
table = pd.crosstab(test_y, cat_probs01 >= threshold, rownames=['label'], colnames=['preds'])
print(table)
print('模型test f1得分:')
f1(table.iloc[1, 1] / table.iloc[:, 1].sum(), table.iloc[1, 1] / table.iloc[1, :].sum())
origin_fraud = round((table.iloc[1, :].sum()) / (table.iloc[:, 0].sum() + table.iloc[:, 1].sum()), 4)
fraud = round(table.iloc[1, 0] / table.iloc[:, 0].sum(), 4)
reject = round((table.iloc[1, 1] + table.iloc[0, 1]) / (table.iloc[:, 0].sum() + table.iloc[:, 1].sum()), 4)

print('建模样本欺诈率：%s' % format(origin_fraud, '.2%'))
print('欺诈率：%s' % format(fraud, '.2%'))
print('拒绝率：%s' % format(reject, '.2%'))

# 实际拒付
test_pdf["prob"] = cat_probs01
ruleRej = test_pdf[test_pdf["风控决策结果"] != "Reject"]

print(min(ruleRej.prob), max(ruleRej.prob))
table = pd.crosstab(ruleRej.label, ruleRej.prob >= threshold, rownames=['label'], colnames=['preds'])
print(table)
print('模型test f1得分:')
f1(table.iloc[1, 1] / table.iloc[:, 1].sum(), table.iloc[1, 1] / table.iloc[1, :].sum())
origin_fraud = round((table.iloc[1, :].sum()) / (table.iloc[:, 0].sum() + table.iloc[:, 1].sum()), 4)
fraud = round(table.iloc[1, 0] / table.iloc[:, 0].sum(), 4)
reject = round((table.iloc[1, 1] + table.iloc[0, 1]) / (table.iloc[:, 0].sum() + table.iloc[:, 1].sum()), 4)

print('建模样本欺诈率：%s' % format(origin_fraud, '.2%'))
print('欺诈率：%s' % format(fraud, '.2%'))
print('拒绝率：%s' % format(reject, '.2%'))

plt.figure(figsize=(10, 10))
# precision,recall,threshold = precision_recall_curve(test_y,cat_probs01,pos_label=1)
# precision,recall,threshold = precision_recall_curve(train_y,pred_train,pos_label=1)
precision, recall, threshold = precision_recall_curve(valid_y, pred_valid, pos_label=1)
plt.plot(recall, precision)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.7, 1.0])
plt.show()


# 不同阈值下的评价指标
def getDiffThresholdPR(threshold, label, pred):
    table = pd.crosstab(label, pred >= threshold, rownames=['label'], colnames=['preds'])
    p = table.iloc[1, 1] / table.iloc[:, 1].sum()
    r = table.iloc[1, 1] / table.iloc[1, :].sum()
    f1 = 2 * p * r / (p + r)
    return (p, r, f1)


# thresholds = [0.1,0.2,0.3,0.4]
thresholds = [x / 100 for x in range(10, 100, 5)]
prfList = []
for threshold in thresholds:
    validP, validR, validF = getDiffThresholdPR(threshold, valid_y, pred_valid)
    testP, testR, testF = getDiffThresholdPR(threshold, test_y, cat_probs01)
    prfList.append([threshold, validP, validR, validF, testP, testR, testF])
prfPdf = pd.DataFrame(prfList,
                      columns=["threshold", "validPrecisoin", "validRecall", "validF1", "testPrecisoin", "testRecall",
                               "testF1"])

testModelPdf["prob"] = cat_probs01
orderPdf = testModelPdf[["业务订单号", "交易流水号", "label", "风控决策结果", "prob"]]
orderPdf = orderPdf.drop_duplicates(subset=["业务订单号"], keep="last")

n = len(orderPdf)
orderPdf.loc[:, 'threshold'] = pd.cut(orderPdf['prob'], bins=[float('-inf')] + thresholds, labels=thresholds,
                                      right=False)
groupOrderPdf = orderPdf.groupby(['threshold'])["业务订单号"].count().reset_index()
groupOrderPdf["acceptRatio"] = groupOrderPdf["业务订单号"].cumsum() / n
groupOrderPdf = groupOrderPdf[["threshold", "acceptRatio"]]
pd.merge(prfPdf, groupOrderPdf, on="threshold")
