#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/03/16 16:47:47
@Author  : pengyuan.li
@File    : 01-highFreqs.py
@Software: VSCode
'''

# here put the import lib
import pandas as pd
import jieba
from collections import Counter
def getWordFreqs(text):
    words = jieba.cut(text)
    freqs = Counter(list(words))
    print(freqs)
    pass

if __name__ == '__main__':
    pdf = pd.read_csv('./xwlb/out.csv')
    getWordFreqs(pdf.loc[0,'details'])
    # print(pdf.head())
    