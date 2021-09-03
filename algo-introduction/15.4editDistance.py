#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 下午3:50
# @Author  : pengyuan.li
# @Site    : 
# @File    : 15.4editDistance.py
# @Software: PyCharm


def Levenshtein_Distance(str1, str2):
    """
    计算字符串 str1 和 str2 的编辑距离
    :param str1
    :param str2
    :return:
    """
    matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + d)

    return matrix[len(str1)][len(str2)] / max(len(str1), len(str2))


s1 = "0481 joao maciel filho haroldo camilo 481"
s2 = "aven joao maciel filho 40801 haroldo camilo 481"

s1 = "alessandra silva"
s2 = "alessandra silva"
print(Levenshtein_Distance(s1, s2), max(len(s1), len(s2)))

# 编辑距离越小，两字段越相似
