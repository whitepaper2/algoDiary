#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 下午7:06
# @Author  : pengyuan.li
# @Site    : 
# @File    : 33.1_crossLine.py
# @Software: PyCharm

"""
判断两线段是否相交
"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.y - self.y * other.x


def isCross(p1, p2, p3, p4):
    """
    1、相交的充要条件：叉积<0
    2、若叉积=0，则需判断是否线段上
    :param p1:
    :param p2:
    :param p3:
    :param p4:
    :return:
    """

    def direction(pi, pj, pk):
        """
        (pk-pi)与(pj-pi)的相对位置，
        :param pi:
        :param pj:
        :param pk:
        :return:
        """
        return (pk - pi) * (pj - pi)

    def segment(pi, pj, pk):
        if min(pi.x, pj.x) <= pk.x <= max(pi.x, pj.x) and min(pi.y, pj.y) <= pk.y <= max(pi.y, pj.y):
            return True
        return False

    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)
    if d1 * d2 < 0 and d3 * d4 < 0:
        return True
    if d1 == 0 and segment(p3, p4, p1):
        return True
    elif d2 == 0 and segment(p3, p4, p2):
        return True
    elif d3 == 0 and segment(p1, p2, p3):
        return True
    elif d4 == 0 and segment(p1, p2, p4):
        return True
    else:
        return False


if __name__ == "__main__":
    points = [[0, 0], [2, 2], [1, 1], [0, 2]]
    inputs = list()
    for x, y in points:
        inputs.append(Point(x, y))
    print(isCross(inputs[0], inputs[1], inputs[2], inputs[3]))
