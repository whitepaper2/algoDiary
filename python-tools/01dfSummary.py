#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 下午3:39
# @Author  : pengyuan.li
# @Site    : 
# @File    : 01dfSummary.py
# @Software: PyCharm
from datetime import datetime
import pandas as pd
import numpy as np


# 生成df的基本统计信息：分位数、top5


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
    return op


def get_data_summary(da):
    op = pd.concat([pd.DataFrame({"type": da.dtypes, "n": da.notnull().sum(axis=0)}), da.describe().T.iloc[:, 1:],
                    pd.concat(map(lambda i: value_counts(da.loc[:, i]), da.columns))], axis=1).loc[da.columns]
    op.index.name = "Columns"
    # return op
    create_time = datetime.now().strftime("%Y%m%d%H%M%S")
    op.to_csv("./data_summary{}.csv".format(create_time))


if __name__ == "__main__":
    df = pd.DataFrame(
        {'name': ["老王", "老张", "老何", "老魏", "老许"], 'age': [24, 18, 36, 67, 38], 'weight': [46, 57, 32, 64, 53]})
    get_data_summary(df)
