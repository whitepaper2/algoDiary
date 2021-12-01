#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 下午3:54
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1.4subSum.py
# @Software: PyCharm


def subSum(A, k):
    """
    判断是否可以从数组A中选出若干个，和=k
    并不能用回溯法求解，因为该方法是在解空间中寻找一组解。
    :param A:
    :param k:
    :return:
    """
    n = len(A)
    vis = [0] * len(A)

    def trackBack(step, cur, visited):
        """
        修改后的回溯法，其原理和dfs相同，分为使用和不使用当前数值两种情况
        :param step:
        :param cur:
        :param visited:
        :return:
        """
        if step > n:
            return
        if step == n:
            # return list(cur)
            return sum(list(cur)) == k
        for i, e in enumerate(A):
            if not visited[i]:
                # 使用A[i]
                cur.append(e)
                visited[i] = 1
                if trackBack(step + 1, cur, visited):
                    return True
                cur.pop()
                visited[i] = 0
                # 不使用A[i]
                visited[i] = 1
                if trackBack(step + 1, cur, visited):
                    return True
                visited[i] = 0
        return False

    return trackBack(0, [], vis)


def subSum2(A, k):
    """
    判断是否可以从数组A中选出若干个，和=k
    :param A:
    :param k:
    :return:
    """
    n = len(A)

    def dfs(step, curSum):
        if step == n:
            return curSum == k
        if dfs(step + 1, curSum):
            return True
        if dfs(step + 1, curSum + A[step]):
            return True
        return False

    return dfs(0, 0)


def subSum3(A, k):
    """
    判断是否可以从数组A中选出若干个，和=k
    优化方法：提前剪枝
    :param A:
    :param k:
    :return:
    """
    n = len(A)
    A.sort(reverse=True)
    from functools import lru_cache

    @lru_cache()
    def dfs(step, curSum):
        if curSum > k:
            return False
        if curSum == k:
            return True
        if step == n:
            return curSum == k
        if dfs(step + 1, curSum):
            return True
        if dfs(step + 1, curSum + A[step]):
            return True
        return False

    return dfs(0, 0)


if __name__ == "__main__":
    nums = [1, 2, 4, 7]
    k = 13
    print(subSum(nums, k))

    print(subSum2(nums, k))

    print(subSum3(nums, k))
