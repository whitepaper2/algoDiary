#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 下午7:20
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200512_min_stack.py
# @Software: PyCharm

import math


class MinStack:
# 维护一个最小元素表
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.min_nums = [math.inf]

    def push(self, x: int) -> None:
        self.nums.append(x)
        self.min_nums.append(min(x, self.min_nums[-1]))

    def pop(self) -> None:
        self.nums.pop()
        self.min_nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min_nums[-1]


class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    # 得到最小值
    def getMin(self) -> int:
        return min(self.nums)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())  # --> 返回 -3.
obj.pop()
print(obj.top())  # --> 返回 0.
print(obj.getMin())  # --> 返回 -2.

# for v in [2, 3, 4, 1, 5, 6, 9]:
#     obj.push(v)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# print(param_3, param_4)
