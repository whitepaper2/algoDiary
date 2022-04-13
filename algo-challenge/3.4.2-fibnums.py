#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/04/13 11:20:07
@Author  : pengyuan.li
@File    : 3.4.2-fibnums.py
@Software: VSCode
'''

# here put the import lib
# f(0)=0
# f(1)=1
# f(n+2)=f(n+1)+f(n)
# 上述即是斐波那契数列的递推式，朴素算法：O(n);改为矩阵求幂，O(logn)


def fibNums(n):
    A = [[1, 1], [1, 0]]

    def _matAB(A, B):
        C = [[0] * len(A) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A)):
                for k in range(len(A)):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def _multipA(A, n):
        if n<=0:
            return [[1,0],[0,1]]
        elif n==1:
            return A
        C = _multipA(A, n // 2)
        res = _matAB(C, C)
        if n % 2 == 1:
            res = _matAB(res, A)
        return res

    B = _multipA(A, n)
    return B[1][0]


if __name__ == "__main__":
    n = 10
    print(fibNums(n))
