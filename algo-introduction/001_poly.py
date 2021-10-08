#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 下午10:38
# @Author  : pengyuan.li
# @Site    : 
# @File    : 001_poly.py
# @Software: PyCharm


def poly(A, x, n):
    """
    note:多项式计算方法，honer法则
    :param A:
    :param x:
    :param n:
    :return:
    """
    res = A[0]
    for i in range(1, n):
        res = res * x + A[i]
    return res


import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.linspace(-10, 10, 10000)
y = np.linspace(-10, 10, 10000)
s = 0.7 * x + 0.3 * y
ax.plot(x, y, s, label='parametric curve')
ax.legend()
plt.show()

# cset = ax.contour(x, y, s, cmap=cm.coolwarm)
# ax.clabel(cset, fontsize=9, inline=1)
#
# plt.show()
# if __name__ == "__main__":
#     A = [2, 3, 4, 1]
#     n = 4
#     x = 2
#
#     print(poly(A, x, n))
