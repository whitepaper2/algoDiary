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
    def __init__(self, left=None, right=None, maxVal=None):
        self.left = left
        self.right = right
        self.maxVal = maxVal


class SegmentTree(object):
    def __init__(self):
        self.maxN = 100
        self.A = [TreeNode() for _ in range(self.maxN)]
        self.idx = {}

    def _buildOneStep(self, p, l, r, nums):
        self.idx[(l, r)] = p
        self.A[p].left = l
        self.A[p].right = r
        if l == r:
            self.A[p].maxVal = nums[l]
            return
        mid = (l + r) // 2
        self._buildOneStep(2 * p, l, mid, nums)
        self._buildOneStep(2 * p + 1, mid + 1, r, nums)
        self.A[p].maxVal = max(self.A[2 * p].maxVal, self.A[2 * p + 1].maxVal)

    def build(self, nums):
        n = len(nums)
        nums.insert(0, 0)
        self._buildOneStep(1, 1, n, nums)

    def change(self, i, v):
        """
        nums[i] = v，先找到i在树中的位置，更新其父节点
        :param i:
        :param v:
        :return:
        """
        p = self.idx[(i, i)]
        self.A[p].maxVal = v
        while p // 2 > 0:
            self.A[p // 2].maxVal = max(self.A[p // 2].maxVal, self.A[p].maxVal)
            p = p // 2

    def change2(self, p, i, v):
        """
        nums[i] = v
        :param i:
        :param v:
        :return:
        """
        if self.A[p].left == self.A[p].right:
            self.A[p].maxVal = v
            return
        mid = (self.A[p].left + self.A[p].right) // 2
        if i <= mid:
            self.change2(2 * p, i, v)
        else:
            self.change2(2 * p + 1, i, v)
        self.A[p].maxVal = max(self.A[2 * p].maxVal, self.A[2 * p + 1].maxVal)

    def ask(self, l, r):
        """
        [l,r]区间查询最值
        :param l:
        :param r:
        :return:
        """
        if (l, r) in self.idx:
            return self.A[self.idx[(l, r)]].maxVal
        mid = (l + r) // 2
        return max(self.ask(l, mid), self.ask(mid + 1, r))

    def ask2(self, p, l, r):
        """
        [l,r]区间查询最值
        :param l:
        :param r:
        :return:
        """
        # 完全包含，候选答案
        if self.A[p].left >= l and self.A[p].right <= r:
            return self.A[p].maxVal
        mid = (self.A[p].left + self.A[p].right) // 2
        val = float('-inf')
        # 不用单独拆边，只要与节点有重叠
        if l <= mid:
            val = max(val, self.ask2(2 * p, l, r))
        if r > mid:
            val = max(val, self.ask2(2 * p + 1, l, r))
        return val


if __name__ == "__main__":
    nums = [3, 6, 4, 8, 1, 2, 9, 5, 7, 0]
    segtree = SegmentTree()

    segtree.build(nums)
    print(segtree.ask(2, 5))

    segtree.change(7, 1)
    print(segtree.ask(2, 5))

    segtree.change2(1, 7, 1)
    print(segtree.ask2(1, 2, 5))
