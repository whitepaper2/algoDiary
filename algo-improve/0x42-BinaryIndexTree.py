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
        单点查询，[1-i]求和
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
        单点增加，在 A[i] += y
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


def getVCnts(nums):
    """
    楼兰图腾，计算 V 型个数
    遍历每个数，分别计算 left[i]\right[i]，左边\右边大于nums[i]的个数，最后再求和
    :param nums: [1,2,...,n]的一个排列
    :return:
    """
    # n = len(nums)
    # left = [0] * n
    # right = [0] * n
    # # 右边比当前值小的个数
    # bst = BinIndexTree()
    # for i in range(n - 1, -1, -1):
    #     right[i] += bst.ask(nums[i] - 1)
    #     bst.addByOne(nums[i], 1)
    # # 左边比当前值小的个数
    # bst = BinIndexTree()
    # for i in range(n):
    #     left[i] += bst.ask(nums[i] - 1)
    #     bst.addByOne(nums[i], 1)

    n = len(nums)
    left = [0] * n
    right = [0] * n
    # 右边比当前值大的个数
    bst = BinIndexTree()
    for i in range(n - 1, -1, -1):
        right[i] += bst.ask(n) - bst.ask(nums[i] - 1)
        bst.addByOne(nums[i], 1)
    # 左边比当前值大的个数
    bst = BinIndexTree()
    for i in range(n):
        left[i] += bst.ask(n) - bst.ask(nums[i] - 1)
        bst.addByOne(nums[i], 1)
    res = 0
    for p, q in zip(left, right):
        print(p, q)
        res += p * q
    return res


def getVCnts2(nums):
    """
    楼兰图腾，计算 V 型个数
    遍历每个数，分别计算 left[i]\right[i]，左边\右边大于nums[i]的个数，最后再求和
    :param nums: [1,2,...,n]的一个排列
    :return:
    """
    n = len(nums)
    bst = BinIndexTree()
    leftLower = [0] * (n + 1)
    leftGreater = [0] * (n + 1)
    for i, e in enumerate(nums):
        leftLower[i + 1] = bst.ask(e - 1)
        leftGreater[i + 1] = bst.ask(n) - bst.ask(e)
        bst.addByOne(e, 1)
    resA = 0
    resV = 0
    bst = BinIndexTree()
    for i in range(len(nums) - 1, -1, -1):
        resA += leftLower[i + 1] * bst.ask(nums[i] - 1)
        resV += leftGreater[i + 1] * (bst.ask(n) - bst.ask(nums[i]))
        bst.addByOne(nums[i], 1)
    return resA, resV


def tinyProblem(nums, commands):
    """
    第一类指令形如 C l r d，表示把数列中第 l∼r 个数都加 d。
    第二类指令形如 Q x，表示询问数列中第 x 个数的值。
    对于每个询问，输出一个整数表示答案。
    :param nums:下标从1开始
    :param commands: 指令集合
    :return:
    """
    nums.insert(0, 0)
    bitInstance = BinIndexTree()
    for command in commands:
        if command[0] == 'Q':
            print(nums[command[1]] + bitInstance.ask(command[1]))
        else:
            l, r, v = command[1], command[2], command[3]
            bitInstance.addByOne(l, v)
            bitInstance.addByOne(r + 1, -v)


def tinyProblem2(nums, commands):
    """
    第一类指令形如 C l r d，表示把数列中第 l∼r 个数都加 d。
    第二类指令形如 Q l r，表示询问数列中第 l-r 个数的和。
    对于每个询问，输出一个整数表示答案。
    :param nums:下标从1开始
    :param commands: 指令集合
    :return:
    """
    nums.insert(0, 0)
    from itertools import accumulate
    prefixSum = list(accumulate(nums))
    bitInstance = BinIndexTree()
    bitInstance2 = BinIndexTree()
    for command in commands:
        if command[0] == 'Q':
            l, r = command[1], command[2]
            print(prefixSum[r] + (r + 1) * bitInstance.ask(r) - bitInstance2.ask(r) - (
                    prefixSum[l - 1] + (l - 1) * bitInstance.ask(l - 1) - bitInstance2.ask(l - 1)))
        else:
            l, r, v = command[1], command[2], command[3]
            bitInstance.addByOne(l, v)
            bitInstance.addByOne(r + 1, -v)
            bitInstance2.addByOne(l, l * v)
            bitInstance2.addByOne(r + 1, -v * (r + 1))


if __name__ == "__main__":
    nums = [1, 2, 3, 15, 9, 6]
    bitInstance = BinIndexTree()
    bitInstance.addByList(nums)
    # for i in range(1, len(nums) + 1):
    #     print(bitInstance.ask(i))
    print(bitInstance.askRange(2, 5))
    print(getReverseCnts(nums))

    nums = [1, 5, 3, 2, 4]
    print(getVCnts2(nums))

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    commands = [['Q', 4], ['Q', 1], ['Q', 2], ['C', 1, 6, 3], ['Q', 2]]
    print("-" * 5)
    tinyProblem(nums, commands)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    commands = [['Q', 4, 4], ['Q', 1, 10], ['Q', 2, 4], ['C', 3, 6, 3], ['Q', 2, 4]]
    tinyProblem2(nums, commands)
