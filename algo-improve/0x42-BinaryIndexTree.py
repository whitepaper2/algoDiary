#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 下午4:46
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x42-BinaryIndexTree.py
# @Software: PyCharm


def genSegment(x):
    """
    x的分段
    :param x:
    :return:
    """
    while x > 0:
        print("[{},{}]".format(x - (x & -x) + 1, x))
        x -= x & -x


"""
python 没有32位之分
负数补码表示：原码去反加1，符号位为1.
-2, 执行 n = n & 0xffffffff
bin(-2 & 0xffffffff)
"""


def lowbit(n):
    """
    lowbit(n) = k，第k位=1 and 后面的位值=0所构成的数值
    :param n:
    :return:
    """
    # return n & (~n + 1)
    return n & (-n)


"""
树状数组，维护序列的前缀和
"""


class BinIndexTree(object):
    """
    C[x]保存区间[x-lowbit(x)+1,x]中所有元素和
    """

    def __init__(self):
        self.maxN = 100
        self.C = [0] * self.maxN

    def _lowbit(self, n):
        """
        lowbit(n) = k，第k位=1 and 后面的位值=0所构成的数值
        :param n:
        :return:
        """
        return n & (-n)

    def ask(self, i):
        """
        [1-i]求和
        :param i:
        :return:
        """
        res = 0
        while i > 0:
            res += self.C[i]
            i -= self._lowbit(i)
        return res

    def askRange(self, l, r):
        """
        [l,r]区间和
        :param l:
        :param r:
        :return:
        """
        lval = self.ask(l - 1)
        rval = self.ask(r)
        return rval - lval

    def addByOne(self, i, y):
        """
        在 A[i] += y
        :param i:
        :param y:
        :return:
        """
        while i < self.maxN:
            self.C[i] += y
            i += self._lowbit(i)

    def addByList(self, A):
        """
        下标从1开始计算
        :param A:
        :return:
        """
        i = 1
        for e in A:
            self.addByOne(i, e)
            i += 1


def getReverseCnts(nums):
    """
    数组的逆序对
    :param nums:
    :return:
    """
    res = 0
    bst = BinIndexTree()
    for i in range(len(nums) - 1, -1, -1):
        res += bst.ask(nums[i] - 1)
        bst.addByOne(nums[i], 1)
    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 15, 9, 6]
    bitInstance = BinIndexTree()
    bitInstance.addByList(nums)
    for i in range(1, len(nums) + 1):
        print(bitInstance.ask(i))
    print(bitInstance.askRange(2, 5))
    print(getReverseCnts(nums))
