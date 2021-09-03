#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 下午4:22
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200728_longeststr.py
# @Software: PyCharm

# 是否可以按照目标输出铁路轨迹
def subway(n, target):
    """
    :param n: 5
    :param target: [5,4,3,2,1]
    :return: Yes/No
    """
    stack = list()
    idxA = 1
    idxB = 1
    isok = True
    target.insert(0, -1)
    while idxB <= n:
        if idxA == target[idxB]:
            idxA += 1
            idxB += 1
        elif stack and stack[-1] == target[idxB]:
            stack.pop()
            idxB += 1
        elif idxA < n:
            stack.append(idxA)
            idxA += 1
        else:
            isok = False
            break
    return "Yes" if isok else "No"


if __name__ == "__main__":
    n = 5
    target = [1, 2, 3, 4, 5]
    print(subway(n, target))

    n = 5
    target = [5, 4, 1, 2, 3]
    print(subway(n, target))

    n = 6
    target = [6, 5, 4, 3, 2, 1]
    print(subway(n, target))
