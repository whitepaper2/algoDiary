#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 下午6:58
# @Author  : pengyuan.li
# @Site    : 
# @File    : common.py
# @Software: PyCharm


import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        start = time.time()
        data = func(*args, **kwds)
        end = time.time()
        print('function {} used time :{}ms'.format(func.__name__, (end - start) * 1000))
        # print('function {} used time :{}ms'.format(func.__name__, int(round((end - start) * 1000))))
        return data

    return wrapper


# n = 50
# primes = [True]*(n+1)
# for i in range(2,n):
#     if primes[i]:
#         for j in range(2,n):
#             if i*j>n:
#                 break
#             primes[i*j] = False
# print(primes)

students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
m = len(students)
n = len(students[0])
A = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        print(sum([int(students[i][k] == mentors[i][k]) for k in range(n)]))
        A[i][j] += sum([int(students[i][k] == mentors[i][k]) for k in range(n)])
