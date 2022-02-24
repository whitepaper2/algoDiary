# !/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

#################################### preProcess.py ######################################
dfp = pd.read_csv('./rawdata_up/tdl_aopeng_20210301_20210909.csv', sep='\00')


# dfp = pd.read_csv('./features/dfp_features1.csv')
# 统计分位数和数据分布
def value_counts(das, nhead=5):
    tmp = pd.value_counts(das).reset_index().rename({"index": das.name}, axis=1)
    value = pd.DataFrame(['value {}'.format(x + 1) for x in range(nhead)], index=np.arange(nhead)).join(tmp.iloc[:, 0],
                                                                                                        how="left").set_index(
        0).T
    freq = pd.DataFrame(['freq {}'.format(x + 1) for x in range(nhead)], index=np.arange(nhead)).join(tmp.iloc[:, 1],
                                                                                                      how="left").set_index(
        0).T
    nnull = das.isnull().sum()
    freqother = pd.DataFrame({das.name: [das.shape[0] - nnull - np.nansum(freq.values), nnull]},
                             index=["freq others", "freq NA"]).T
    op = pd.concat([value, freq, freqother], axis=1)
    return (op)


def get_data_summary(da):
    op = pd.concat([pd.DataFrame({"type": da.dtypes, "n": da.notnull().sum(axis=0)}), da.describe().T.iloc[:, 1:],
                    pd.concat(map(lambda i: value_counts(da.loc[:, i]), da.columns))], axis=1).loc[da.columns]
    op.index.name = "Columns"
    return op


dfpSummary = get_data_summary(dfp)
dfpSummary.to_csv("./features/daSummary.csv")

# 每天的交易量 plot
dfp['eventOccurTime2'] = dfp['eventOccurTime2'].astype(str)
dfp['eventOccurTime2'] = pd.to_datetime(dfp['eventOccurTime2'], format="%Y-%m-%d")
monthLabel = dfp.groupby(["eventOccurTime2"])["交易流水号"].count().reset_index()
xticks = [v for i, v in enumerate(list(monthLabel["eventOccurTime2"])) if i % 20 == 0]
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 8))
plt.plot(monthLabel["eventOccurTime2"], monthLabel["交易流水号"])
plt.xticks(xticks)
plt.show()

# label按时间分布
labelPdf = dfp.groupby(["eventOccurTime2", "label"])["交易流水号"].count().reset_index()
label0Pdf = labelPdf[labelPdf["label"] == 0]
label1Pdf = labelPdf[labelPdf["label"] == 1]
label_1Pdf = labelPdf[labelPdf["label"] == -1]
xticks = [v for i, v in enumerate(list(monthLabel["eventOccurTime2"])) if i % 20 == 0]
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 8))
plt.plot(label0Pdf["eventOccurTime2"], label0Pdf["交易流水号"])
plt.plot(label1Pdf["eventOccurTime2"], label1Pdf["交易流水号"])
plt.plot(label_1Pdf["eventOccurTime2"], label_1Pdf["交易流水号"])
plt.xticks(xticks)
plt.show()

# 客户姓名（测试）
pdf["客户姓名"].value_counts().reset_index().to_csv("./features/accountNameCnts.csv")

#################################### trainModel.py ######################################

corr = model_data.corr()
cols = list(corr.columns)
n = len(cols)
for r in range(n):
    for c in range(r):
        if r != c and abs(corr.loc[cols[r], cols[c]]) > 0.8:
            print(cols[r], cols[c], corr.loc[cols[r], cols[c]])


# 数据分布情况
def getSampleSummary(desc, pdf):
    total = len(pdf)
    label1 = len(pdf[pdf['label'] == 1])
    ruleReject = len(pdf[pdf["风控决策结果"] == "Reject"])
    return desc, total, label1, round(label1 / total, 4), ruleReject, round(ruleReject / total, 4)


lst = [getSampleSummary("train", train_pdf), getSampleSummary("valid", valid_pdf), getSampleSummary("test", test_pdf)]

colName = ["dataName", "totalNum", "label=1Num", "label=1Ratio", "rule=RejectNum", "rule=RejectRatio"]
descPdf = pd.DataFrame(lst, columns=colName)
print(descPdf)

# PR曲线


def plotPR(desc, true_y, pred_y):
    plt.figure(figsize=(10, 10))
    precision, recall, thresholds = precision_recall_curve(true_y, pred_y, pos_label=1)
    avgPrecision = average_precision_score(true_y, pred_y, average="micro", pos_label=1)

    plt.plot(recall, precision)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.5, 1.0])
    plt.title(desc + 'Precision-Recall curve: AP={0:0.2f}'.format(avgPrecision))

    thresholds = np.insert(thresholds, 0, 0)
    fig, ax = plt.subplots(1, 2, sharey=True, figsize=(20, 10))
    plt.sca(ax[0])
    plt.grid(True)
    plt.plot(precision, thresholds)
    plt.xlabel('Precision')
    plt.ylabel('threshold')
    # plt.ylim([0.0, 1.05])
    # plt.xlim([0.0, 1.0])

    plt.sca(ax[1])
    plt.plot(recall, thresholds)
    plt.xlabel('Recall')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.grid(True)
    plt.show()
    plt.close()


plotPR("train ", train_y, pred_train)
plotPR("valid ", valid_y, pred_valid)
plotPR("test ", test_y, cat_probs01)

# AUC曲线
from sklearn.metrics import precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt


def getPRs():
    p1, r1, _ = precision_recall_curve(train_y, pred_train, pos_label=1)
    avgP1 = average_precision_score(train_y, pred_train, average="micro", pos_label=1)
    p2, r2, _ = precision_recall_curve(valid_y, pred_valid, pos_label=1)
    avgP2 = average_precision_score(valid_y, pred_valid, average="micro", pos_label=1)
    p3, r3, _ = precision_recall_curve(test_y, cat_probs01, pos_label=1)
    avgP3 = average_precision_score(test_y, cat_probs01, average="micro", pos_label=1)
    return [p1, p2, p3], [r1, r2, r3], ['train AP={0:0.2f}'.format(avgP1), 'valid AP={0:0.2f}'.format(avgP2),
                                        'test AP={0:0.2f}'.format(avgP3)]


precisions, recalls, avgPrecisions = getPRs()
plt.figure(figsize=(10, 10))
labels = list()
lines = list()
for p, r, avgp in zip(precisions, recalls, avgPrecisions):
    l, = plt.plot(r, p)
    lines.append(l)
    labels.append(avgp)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.5, 1.0])
plt.legend(lines, labels)
plt.title('Precision-Recall curve')
plt.show()


# 模型抓头部的能力
def tpr_weight_function(y_true, y_predict):
    d = pd.DataFrame()
    d['prob'] = list(y_predict)
    d['y'] = list(y_true)
    d = d.sort_values(['prob'], ascending=[0])
    y = d.y
    PosAll = pd.Series(y).value_counts()[1]
    NegAll = pd.Series(y).value_counts()[0]
    pCumsum = d['y'].cumsum()
    nCumsum = np.arange(len(y)) - pCumsum + 1
    pCumsumPer = pCumsum / PosAll
    nCumsumPer = nCumsum / NegAll
    TR1 = pCumsumPer[abs(nCumsumPer - 0.001).idxmin()]
    TR2 = pCumsumPer[abs(nCumsumPer - 0.005).idxmin()]
    TR3 = pCumsumPer[abs(nCumsumPer - 0.01).idxmin()]
    return 0.4 * TR1 + 0.3 * TR2 + 0.3 * TR3


print("trainTopAcc =", tpr_weight_function(train_y, pred_train))
print("validTopAcc =", tpr_weight_function(valid_y, pred_valid))
print("testTopAcc =", tpr_weight_function(test_y, cat_probs01))

# 特征重要性
importances = model.feature_importances_
lst = zip(train_x.columns, importances)
lst = sorted(lst, key=lambda x: x[1], reverse=True)
print(lst)

# 计算ks
from scipy.stats import ks_2samp
ks_2samp(modelPdf.loc[modelPdf.label==1,'prob'],modelPdf.loc[modelPdf.label==0,'prob'])


def plot_lift(y_predproab, y_true):
    '''
    params:
        y_predproab:预测值概率/正样本分组
        y_true:真实值/正负样本标记label
    result:
        绘制lift曲线
    '''
    result = pd.DataFrame([y_true,y_predproab]).T
    result.columns = ['target','proba']
    result = result.sort_values(['proba','target'],ascending=False).reset_index()
    del result['index']
    result.set_index((result.index+1)/result.shape[0],inplace=True)
    result['bad_sum'] = result['target'].cumsum()
    result['count_sum'] = [i+1 for i in range(result.shape[0])]
    result['rate'] = result['bad_sum']/result['count_sum']
    result['lift'] = result['rate']/(result['target'].sum()/result.shape[0])
    
    fig = plt.figure(figsize=(12,6))
    ax1 = fig.add_subplot(1,2,1)
    ax1.grid(True,linestyle='-.')
    ax1.plot(result['rate'],color='red',label='Lift model')
    ax1.plot(result.index,[result['target'].sum()/result.shape[0]]*result.shape[0],color='blue',label='Lift random')
    ax1.set_title('Lift Chart',fontsize=25)
    ax1.set_ylabel('tp/(tp+fp)',fontsize=20)
    ax1.set_xlabel('data sets',fontsize=20)
    ax1.set_xticks([i/10 for i in range(11)])
    plt.legend(loc='best')
    
    ax2 = fig.add_subplot(1,2,2)
    ax2.plot(result['lift'],color='darkorange')
    ax2.grid(True,linestyle='-.')
    ax2.set_title('Cumulative Lift Chart',fontsize=25)
    ax2.set_ylabel('lift',fontsize=20)
    ax2.set_xlabel('data sets',fontsize=20)
    ax2.set_xticks([i/10 for i in range(11)])
    plt.show()
    
def plot_auc_ks(y,pred):
    from sklearn.metrics import roc_curve
    fpr,tpr,thresholds = roc_curve(y,pred)
    auc=roc_auc_score(y,pred) #计算auc
    print("AUC:",auc)
    
    #计算ks
    KS_max=0
    best_thr=0
    for i in range(len(fpr)):
        if(i==0):
            KS_max=tpr[i]-fpr[i]
            best_thr=thresholds[i]
        elif (tpr[i]-fpr[i]>KS_max):
            KS_max = tpr[i] - fpr[i]
            best_thr = thresholds[i]

    print('最大KS为：',KS_max)
    print('最佳阈值为：',best_thr)
    table = pd.crosstab(y,pred>=best_thr,rownames=['label'],colnames=['preds'])
    print(table)
    #画曲线图
    plt.figure(figsize=(10,10))
    plt.plot(fpr,tpr)
    plt.title('$ROC curve$')
    plt.show()
# 得到特殊点的lift值
def getLift(y_true,y_predproab, thresholds):
    result = pd.DataFrame([y_true,y_predproab]).T
    result.columns = ['target','proba']
    result = result.sort_values(['proba','target'],ascending=False).reset_index()
    del result['index']
    result.set_index((result.index+1)/result.shape[0],inplace=True)
    result['bad_sum'] = result['target'].cumsum()
    result['count_sum'] = [i+1 for i in range(result.shape[0])]
    result['rate'] = result['bad_sum']/result['count_sum']
    result['lift'] = result['rate']/(result['target'].sum()/result.shape[0])
    for t in thresholds:
        tres = result[result.index<=t]
        print(t,tres.iloc[-1]['lift'])
getLift(modelPdf['label'],modelPdf['prob'],[0.001,0.005,0.01])