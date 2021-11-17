#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/17 下午4:37
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x51-takePhoto.py
# @Software: PyCharm


def picturePermutations(k, people):
    """
    从左到右按身高降序排序、从前到后降序排序，求一共能组成多少中排列方式
    :param k:总排数,1<=k<=5
    :param people:长度为k的数组,sum(people)<=30
    :return:
    """
    maxN = 31
    s = people + [0] * (5 - k)
    f = [[[[[0 for _ in range(maxN)] for _ in range(maxN)] for _ in range(maxN)] for _ in range(maxN)] for _ in
         range(maxN)]
    f[0][0][0][0][0] = 1
    # f = [[[0 for _ in range(maxN)] for _ in range(maxN)] for _ in range(maxN)]

    for a in range(s[0] + 1):
        for b in range(min(a, s[1]) + 1):
            for c in range(min(b, s[2]) + 1):
                for d in range(min(c, s[3]) + 1):
                    for e in range(min(d, s[4]) + 1):
                        if a and a - 1 >= b:
                            f[a][b][c][d][e] += f[a - 1][b][c][d][e]
                        if b and b - 1 >= c:
                            f[a][b][c][d][e] += f[a][b - 1][c][d][e]
                        if c and c - 1 >= d:
                            f[a][b][c][d][e] += f[a][b][c - 1][d][e]
                        if d and d - 1 >= e:
                            f[a][b][c][d][e] += f[a][b][c][d - 1][e]
                        if e:
                            f[a][b][c][d][e] += f[a][b][c][d][e - 1]
    return f[s[0]][s[1]][s[2]][s[3]][s[4]]


if __name__ == "__main__":
    k = 1
    people = [30]

    k = 5
    people = [1, 1, 1, 1, 1]
    print(picturePermutations(k, people))

    k = 3
    people = [3, 2, 1]
    print(picturePermutations(k, people))

    k = 4
    people = [5, 3, 3, 1]
    print(picturePermutations(k, people))

    k = 5
    people = [6, 5, 4, 3, 2]

    k = 2
    people = [15, 15]
