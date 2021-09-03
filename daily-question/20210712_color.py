#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 下午4:22
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200728_longeststr.py
# @Software: PyCharm


def getColorNums(m, n):
    Mod = 1000000007
    valid = dict()
    for mask in range(3 ** m):
        color = list()
        mm = mask
        for i in range(m):
            color.append(mm % 3)
            mm //= 3
        if any(color[i] == color[i + 1] for i in range(m - 1)):
            continue
        valid[mask] = color
        color.sort()
    # return valid
    import collections
    adjacent = collections.defaultdict(list)
    for mask1, color1 in valid.items():
        for mask2, color2 in valid.items():
            if not any([x == y for x, y in zip(color1, color2)]):
                adjacent[mask1].append(mask2)
    f = [int(mask in valid) for mask in range(3 ** m)]
    for i in range(1, n):
        g = [0] * (3 ** m)
        for mask2 in valid.keys():
            for mask1 in adjacent[mask2]:
                g[mask2] += f[mask1]
                if g[mask2] >= Mod:
                    g[mask2] -= Mod
        f = g
    return sum(f) % Mod

from typing import List
class AB:

    def maxPoints(self, points:List[List[int]]):
        m = len(points)
        n = len(points[0])
        self.res = float('-inf')

        def trackBack(step, cur):
            if len(cur) > m:
                return
            elif len(cur) == m:
                curSum = 0

                for i in range(len(cur)):
                    curSum += cur[i][0]
                    if i > 0:
                        curSum -= abs(cur[i][1] - cur[i - 1][1])
                if curSum > self.res:
                    print(self.res,cur)
                    self.res = curSum

            else:
                for i in range(n):
                    cur.append([points[step][i], i])
                    trackBack(step + 1, cur)
                    cur.pop()

        cur = []
        trackBack(0, cur)
        print(self.res)
        return self.res


if __name__ == "__main__":
    # print(getColorNums(5, 1000))
    points2 = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    ab = AB()
    print(ab.maxPoints(points2))
