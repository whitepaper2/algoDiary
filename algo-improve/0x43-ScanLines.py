#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 下午3:55
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x43-SegmentTree.py
# @Software: PyCharm


"""
线段树
"""


class TreeNode(object):
    def __init__(self, left=None, right=None, lens=None, cnts=None):
        self.left = left
        self.right = right
        self.lens = lens
        self.cnts = cnts


class SegmentTree(object):
    def __init__(self, raw):
        self.maxN = 100
        self.A = [TreeNode(lens=0, cnts=0) for _ in range(self.maxN)]
        self.idx = {}
        self.raw = raw

    def _buildOneStep(self, p, l, r):
        self.idx[(l, r)] = p
        self.A[p].left = l
        self.A[p].right = r
        if l == r:
            return
        mid = (l + r) // 2
        self._buildOneStep(2 * p, l, mid)
        self._buildOneStep(2 * p + 1, mid + 1, r)

    def build(self):
        n = len(self.raw)
        self._buildOneStep(1, 0, n)

    def change(self, p, l, r, v):
        """
        nums[i] += v
        :param i:
        :param v:
        :return:
        """
        if l <= self.A[p].left and self.A[p].right <= r:
            self.A[p].cnts = v
            self.pushup(p)
        else:
            mid = (self.A[p].left + self.A[p].right) // 2
            if l <= mid:
                self.change(2 * p, l, r, v)
            if r >= mid + 1:
                self.change(2 * p + 1, l, r, v)
            self.pushup(p)

    def pushup(self, p):
        if self.A[p].cnts > 0:
            self.A[p].lens = self.raw[self.A[p].right + 1] - self.raw[self.A[p].left]
        elif self.A[p].left == self.A[p].right:
            self.A[p].lens = 0
        else:
            self.A[p].lens = self.A[p << 1].lens + self.A[p << 1 | 1].lens

    def ask(self, p):
        """
        位置p查询
        :param l:
        :param r:
        :return:
        """
        return self.A[p].lens


class Line(object):
    def __init__(self, x, y1, y2, k):
        """
        :param x:线的横坐标
        :param y1: lower bound
        :param y2: upper bound
        :param k: left or right boundary
        """
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.k = k

    def __lt__(self, other):
        return self.x < other.x


def scanLines(nums):
    """
    矩形的左下角坐标 (x1,y1) 和右上角坐标 (x2,y2)。
    求矩阵面积并
    :param nums:
    :return:
    """
    lines = []
    raw = set()
    for x1, y1, x2, y2 in nums:
        lines.append(Line(x1, y1, y2, 1))
        lines.append(Line(x2, y1, y2, -1))
        raw.add(y1)
        raw.add(y2)
    raw = list(raw)
    raw.sort()
    raw2idx = dict()
    for i, e in enumerate(raw):
        raw2idx[e] = i
    lines.sort()
    segtree = SegmentTree(raw)
    segtree.build()
    res = 0
    for i in range(len(raw2idx)):
        if i > 0:
            res += segtree.ask(1) * (lines[i].x - lines[i - 1].x)
        segtree.change(1, raw2idx[lines[i].y1], raw2idx[lines[i].y2] - 1, lines[i].k)

    return res


if __name__ == "__main__":
    nums = [[10, 10, 20, 20], [15, 15, 25, 25]]
    print(scanLines(nums))
