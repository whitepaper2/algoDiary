#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 下午3:13
# @Author  : pengyuan.li
# @Site    : 
# @File    : week265.py
# @Software: PyCharm

"""
2059. 转化数字的最小运算数
给你一个下标从 0 开始的整数数组 nums ，该数组由 互不相同 的数字组成。另给你两个整数 start 和 goal 。

整数 x 的值最开始设为 start ，你打算执行一些运算使 x 转化为 goal 。你可以对数字 x 重复执行下述运算：

如果 0 <= x <= 1000 ，那么，对于数组中的任一下标 i（0 <= i < nums.length），可以将 x 设为下述任一值：

x + nums[i]
x - nums[i]
x ^ nums[i]（按位异或 XOR）
注意，你可以按任意顺序使用每个 nums[i] 任意次。使 x 越过 0 <= x <= 1000 范围的运算同样可以生效，但该该运算执行后将不能执行其他运算。

返回将 x = start 转化为 goal 的最小操作数；如果无法完成转化，则返回 -1 。

"""
from collections import deque
from typing import List


def minimumOperations(nums: List[int], start: int, goal: int) -> int:
    """
    没有想到bfs，无权图的最小路径
    :param nums:
    :param start:
    :param goal:
    :return:
    """
    op1 = lambda x, y: x + y
    op2 = lambda x, y: x - y
    op3 = lambda x, y: x ^ y
    ops = [op1, op2, op3]
    visited = [False] * 1001
    queue = deque()
    queue.append((start, 0))
    while queue:
        x, step = queue.popleft()
        for y in nums:
            for op in ops:
                cur = op(x, y)
                if cur == goal:
                    return step + 1
                if 0 <= cur <= 1000 and not visited[cur]:
                    visited[cur] = True
                    queue.append((cur, step + 1))
    return -1


"""
2060. 同源字符串检测
原字符串由小写字母组成，可以按下述步骤编码：

任意将其 分割 为由若干 非空 子字符串组成的一个 序列 。
任意选择序列中的一些元素（也可能不选择），然后将这些元素替换为元素各自的长度（作为一个数字型的字符串）。
重新 顺次连接 序列，得到编码后的字符串。
例如，编码 "abcdefghijklmnop" 的一种方法可以描述为：

将原字符串分割得到一个序列：["ab", "cdefghijklmn", "o", "p"] 。
选出其中第二个和第三个元素并分别替换为它们自身的长度。序列变为 ["ab", "12", "1", "p"] 。
重新顺次连接序列中的元素，得到编码后的字符串："ab121p" 。
给你两个编码后的字符串 s1 和 s2 ，由小写英文字母和数字 1-9 组成。如果存在能够同时编码得到 s1 和 s2 原字符串，返回 true ；否则，返回 false。

注意：生成的测试用例满足 s1 和 s2 中连续数字数不超过 3 。

"""


def possiblyEquals(s1: str, s2: str) -> bool:
    s1Len = len(s1)
    s2Len = len(s2)
    dp = [[0] * (s2Len + 1) for _ in range(s1Len + 1)]
    for i in range(s1Len + 1):
        for j in range(s2Len + 1):
            dp[i][j] = set()
    dp[0][0].add(0)
    for i in range(s1Len + 1):
        for j in range(s2Len + 1):
            for delta in dp[i][j]:
                # 1.dp[i][j]->dp[p][j], delta->delta+num
                num = 0
                for p in range(i, min(i + 3, s1Len)):
                    if s1[p].isdigit():
                        num = 10 * num + int(s1[p])
                        dp[p + 1][j].add(num + delta)
                    else:
                        break
                # 2.dp[i][j]->dp[i][q], delta->delta-num
                num = 0
                for q in range(j, min(j + 3, s2Len)):
                    if s2[q].isdigit():
                        num = 10 * num + int(s2[q])
                        dp[i][q + 1].add(delta - num)
                    else:
                        break
                # 3.dp[i][j]->dp[i+1][j], delta->delta+1
                if i < s1Len and delta < 0 and not s1[i].isdigit():
                    dp[i + 1][j].add(delta + 1)
                # 4.dp[i][j]->dp[i][j+1], delta->delta-1
                if j < s2Len and delta > 0 and not s2[j].isdigit():
                    dp[i][j + 1].add(delta - 1)
                # 5.dp[i][j]->dp[i+1][j+1], delta->delta
                if i < s1Len and j < s2Len and delta == 0 and s1[i] == s2[j]:
                    dp[i + 1][j + 1].add(0)
    return list(dp[s1Len][s2Len]).count(0) > 0


if __name__ == "__main__":
    nums = [3, 5, 7]
    start = 0
    goal = -4
    print(minimumOperations(nums, start, goal))

    s1 = "l123e"
    s2 = "44"
    print(possiblyEquals(s1, s2))
