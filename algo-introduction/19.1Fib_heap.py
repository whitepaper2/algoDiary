#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 下午3:25
# @Author  : pengyuan.li
# @Site    : 
# @File    : 16.3huffman.py
# @Software: PyCharm


class FibNode(object):
    def __init__(self, key):
        """
        初始化 FibNode
        :param key:
        """
        self.key = key
        self.p = None
        self.degree = 0
        self.child = None
        self.left = None
        self.right = None
        self.mark = False


class Fib(object):
    def __init__(self, n, minx):
        """
        初始化
        :param n: 节点个数
        :param minx: 当前最小值
        """
        self.n = n
        self.min = minx

    def insert(self, x):
        """
        增加节点 x=FibNode()
        :param x:
        :return:
        """
        if self.min == 0:
            self.min = x
            x.left = x
            x.right = x
        else:
            x.right = self.min
            x.left = self.min.left
            x.left.right = x
            if x.key < self.min.key:
                self.min = x
        self.n += 1

    def minimum(self):
        """
        返回当前最小节点FibNode
        :return:
        """
        return self.min

    def extract_min(self):
        """
        抽取最小节点，重新把空白的节点给填上
        :return: FibNode
        """
        pass


import random
from random import shuffle


def prepare():
    array = []
    number = 0
    for i in range(200):
        number = number + random.randint(1, 4)
        # number = number + 1
        array.append(number)
    shuffle(array)
    return array


if __name__ == '__main__':
    fib = Fib(0, 0)
    array = prepare()
    for i in array:
        keyword = FibNode(i)
        fib.insert(keyword)
    print(fib.minimum())
