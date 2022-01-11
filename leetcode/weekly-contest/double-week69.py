#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/11 16:01:00
@Author  : pengyuan.li
@File    : double-week69.py
@Software: VSCode
'''

# here put the import lib

from typing import List


class Solution:

    def possibleToStamp(self, grid: List[List[int]], stampHeight: int,
                        stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        def build2dPresum(arr: List[List[int]]) -> List[List[int]]:
            '''
            description: 
            param {*}
            return {*}
            '''
            """
            计算2维前缀和
            """
            m, n = len(arr), len(arr[0])
            preSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    preSum[i + 1][j + 1] = preSum[i + 1][j] + preSum[i][
                        j + 1] - preSum[i][j] + arr[i][j]
            return preSum

        def query(arr, u, l, d, r):
            return arr[d][r] - arr[d][l - 1] - arr[u - 1][r] + arr[u - 1][l -
                                                                          1]

        pSum = build2dPresum(grid)
        paint = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i + stampHeight <= m and j + stampWidth <= n:
                    if grid[i][j] == 0 and query(pSum, i + 1, j + 1,
                                                 i + stampHeight,
                                                 j + stampWidth) == 0:
                        paint[i][j] = 1
        p2Sum = build2dPresum(paint)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and query(p2Sum, max(
                        1, i - stampHeight + 2), max(1, j - stampWidth + 2),
                                             i + 1, j + 1) == 0:
                    return False
        return True


if __name__ == "__main__":
    grid = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0],
            [1, 0, 0, 0]]
    stampHeight = 4
    stampWidth = 3
    ss = Solution()
    print(ss.possibleToStamp(grid, stampHeight, stampWidth))

    grid = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    stampHeight = 2
    stampWidth = 2
    ss = Solution()
    print(ss.possibleToStamp(grid, stampHeight, stampWidth))
