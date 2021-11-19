#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 下午1:59
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x53-mergeStones.py
# @Software: PyCharm


def mergeStones(A):
    """
    合并相邻的石子
    :param A:
    :return:
    """
    n = len(A)
    preSum = [0] * (n + 1)
    f = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        preSum[i] = preSum[i - 1] + A[i - 1]
        f[i][i] = 0

    for step in range(1, n):
        for l in range(1, n - step + 1):
            r = l + step
            for k in range(l, r):
                f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r])
            f[l][r] += preSum[r] - preSum[l - 1]
    return f[1][n]


def polyScores(A):
    """
    t -7 t 4 x 2 x 5
    :param A:
    :return:
    """
    n = len(A)
    N = n // 2
    nums, ops = [], []
    for i in range(0, n, 2):
        ops.append(A[i])
        nums.append(A[i + 1])
    nums += nums
    ops += ops
    nums.insert(0, 0)
    ops.insert(0, 0)
    print(nums, ops)
    fmax = [[float('-inf') for _ in range(n + 1)] for _ in range(n + 1)]
    fmin = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        fmax[i][i] = nums[i]
        fmin[i][i] = nums[i]
    for step in range(1, N + 1):
        for l in range(1, n - step + 1):
            r = step + l
            for k in range(l, r):
                if ops[k + 1] == 'x':
                    fmin[l][r] = min(fmin[l][r], fmin[l][k] * fmin[k + 1][r], fmax[l][k] * fmin[k + 1][r],
                                     fmin[l][k] * fmax[k + 1][r])
                    fmax[l][r] = max(fmax[l][r], fmax[l][k] * fmax[k + 1][r], fmin[l][k] * fmin[k + 1][r])
                else:
                    fmin[l][r] = min(fmin[l][r], fmin[l][k] + fmin[k + 1][r])
                    fmax[l][r] = max(fmax[l][r], fmax[l][k] + fmax[k + 1][r])
    print(fmax)
    return max(fmax[i][i + N - 1] for i in range(1, n + 1, N))


def partyHappiness(happiness, relations):
    """
    :param happiness:开心指数
    :param relations: 上下级关系
    :return:
    """
    from collections import defaultdict
    n = len(happiness)
    happiness.insert(0, 0)
    sons = defaultdict(list)
    visited = [0] * (n + 1)
    for son, parent in relations:
        sons[parent].append(son)
        visited[son] = 1
    root = 0
    for i in range(1, n + 1):
        if visited[i] == 0:
            root = i
    # 不选择当前节点得到最大值、选择当前节点得到最大值
    dp0, dp1 = [0] * (n + 1), [0] * (n + 1)

    def dfs(x):
        dp0[x] = 0
        dp1[x] = happiness[x]
        for y in sons[x]:
            dfs(y)
            dp0[x] += max(dp0[y], dp1[y])
            dp1[x] += dp0[y]

    dfs(root)
    return max(dp0[root], dp1[root])


if __name__ == "__main__":
    nums = [1, 3, 5, 2]
    print(mergeStones(nums))

    ops = ['t', -7, 't', 4, 'x', 2, 'x', 5]
    print(polyScores(ops))

    happiness = [1, 1, 1, 1, 1, 1, 1]
    relations = [[1, 3], [2, 3], [6, 4], [7, 4], [4, 5], [3, 5]]
    print(partyHappiness(happiness, relations))
