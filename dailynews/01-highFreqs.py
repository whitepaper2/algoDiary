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
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from jieba import analyse
import os

stopwordPath = "./dailynews/datasets/cn_stopwords.txt"
userdictPath = "./dailynews/datasets/THUOCL/allthuocl.txt"


def stripStopWords(sentence):
    f = open(stopwordPath, 'r+', encoding='utf-8')
    stopWords = f.read().strip("\n")
    res = []
    for word in sentence:
        if word not in stopWords:
            res.append(word)
    f.close()
    return res


def getWordFreqs(text):
    words = jieba.cut(text)
    jieba.load_userdict(userdictPath)
    filterWords = stripStopWords(list(words))
    freqs = Counter(filterWords)
    return freqs


def plotWordDist(text):
    words = jieba.cut(text)
    filterWords = stripStopWords(list(words))
    # 步骤3-2：设置一张词云图对象
    wordcloud = WordCloud(font_path='./dailynews/font/SimHei.ttf',
                          background_color="white",
                          max_font_size=40).generate(" ".join(filterWords))

    # 步骤4-1：创建一个图表画布
    plt.figure()
    # 步骤4-2：设置图片
    plt.imshow(wordcloud, interpolation="bilinear")
    # 步骤4-3：取消图表x、y轴
    plt.axis("off")
    # 显示图片
    plt.show()


def getKeyWrodsBytfidf(text):
    # 新建 TFIDF 实例，idf_path 为 IDF 频率文件
    # analyse.TFIDF()
    analyse.set_stop_words(stopwordPath)
    res = analyse.extract_tags(text, withWeight=True)

    trank = analyse.TextRank()
    res2 = trank.extract_tags(text, withWeight=True)
    return res, res2


def genDictByThuocl():
    # 中文词典，https://github.com/thunlp/THUOCL
    path = "./dailynews/datasets/THUOCL"
    outfileName = 'allthuocl.txt'
    outfile = open(os.path.join(path, outfileName), 'w')
    for f in os.listdir(path):
        if f == outfileName:
            continue
        print("execute {} ...".format(f))
        file = open(os.path.join(path, f), 'r')
        for lines in file.readlines():
            outfile.write(lines)
    outfile.close()
    print("finished!")


if __name__ == '__main__':
    # f = open("./dailynews/datasets/THUOCL_animal.txt", 'r+')
    # i = 0
    # for line in f.readlines():
    #     if i>10:
    #         break
    #     print(line)
    #     i +=1
    # f = pd.read_csv("./dailynews/datasets/baidudict.txt",sep='\t')
    # print(f.head())
    pdf = pd.read_csv('./xwlb/out.csv')
    print(getWordFreqs(pdf.loc[0, 'details']))
    plotWordDist(pdf.loc[0, 'details'])
    # print(getKeyWrodsBytfidf(pdf.loc[0,'details']))
    # print(pdf.head())
    # genDictByThuocl()
