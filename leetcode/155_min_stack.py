#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 下午11:35
# @Author  : pengyuan.li
# @Site    : 
# @File    : 155_min_stack.py
# @Software: PyCharm


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.val.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.val.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.val[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.val)


# note:维护两个栈，其中一个正常栈，另一个存储最小值
class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val1 = []
        self.val2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.val1.append(x)
        if len(self.val2) == 0 or x < self.val2[-1]:
            self.val2.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.val1[-1] == self.val2[-1]:
            self.val2.pop()
        self.val1.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.val1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.val2[-1]


"""
思路比上面更简单：
1、原始数据和最小点数据存储大小相同
2、取数据之前判断数据是否存在
总之，与一年前相比进步比较明显，还是要多动手写代码和思考
"""


class Stack(object):
    def __init__(self):
        self.rawStack = list()
        self.minStack = list()

    def push(self, x):
        self.rawStack.append(x)
        if self.minStack:
            if self.minStack[-1] < x:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(x)
        else:
            self.minStack.append(x)

    def pop(self):
        if self.rawStack:
            self.rawStack.pop()
            self.minStack.pop()
        else:
            print("error stack is null")

    def top(self):
        if self.rawStack:
            return self.rawStack[-1]
        else:
            print("error stack is null")

    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        else:
            print("error stack is null")


if __name__ == "__main__":
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
    min_stack = MinStack2()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.top())
    print(min_stack.getMin())

    min_stack = Stack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.top())
    print(min_stack.getMin())
