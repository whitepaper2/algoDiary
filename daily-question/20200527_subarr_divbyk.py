#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 下午7:50
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200527_subarr_divbyk.py
# @Software: PyCharm
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        """
        给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
        遍历每个子串求和，是否整除K，time out
        :param A:
        :param K:
        :return:
        """
        len_A = len(A)
        sum_matrix = [[0 for _ in range(len_A)] for _ in range(len_A)]
        out = 0
        for i in range(len_A - 1, -1, -1):
            for j in range(i, len_A):
                if i == j:
                    sum_matrix[i][j] = A[i]
                else:
                    sum_matrix[i][j] = sum_matrix[i + 1][j] + sum_matrix[i][i]
                if sum_matrix[i][j] % K == 0:
                    out = out + 1
        return out

    def subarraysDivByK2(self, A: List[int], K: int) -> int:
        """
        给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
        前缀和 + 同余定理，明天搞定
        :param A:
        :param K:
        :return:
        """
        len_A = len(A)
        sum_matrix = [[0 for _ in range(len_A)] for _ in range(len_A)]
        out = 0
        for i in range(len_A - 1, -1, -1):
            for j in range(i, len_A):
                if i == j:
                    sum_matrix[i][j] = A[i]
                else:
                    sum_matrix[i][j] = sum_matrix[i + 1][j] + sum_matrix[i][i]
                if sum_matrix[i][j] % K == 0:
                    out = out + 1
        return out


if __name__ == "__main__":
    ss = Solution()
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    print(ss.subarraysDivByK(A, K))

    A = [5]
    K = 5
    print(ss.subarraysDivByK(A, K))
