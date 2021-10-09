#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 上午10:38
# @Author  : pengyuan.li
# @Site    : 
# @File    : week261.py
# @Software: PyCharm
"""
2029. 石子游戏 IX
Alice 和 Bob 再次设计了一款新的石子游戏。现有一行 n 个石子，每个石子都有一个关联的数字表示它的价值。给你一个整数数组 stones ，
其中 stones[i] 是第 i 个石子的价值。

Alice 和 Bob 轮流进行自己的回合，Alice 先手。每一回合，玩家需要从 stones 中移除任一石子。

如果玩家移除石子后，导致 所有已移除石子 的价值 总和 可以被 3 整除，那么该玩家就 输掉游戏 。
如果不满足上一条，且移除后没有任何剩余的石子，那么 Bob 将会直接获胜（即便是在 Alice 的回合）。
假设两位玩家均采用 最佳 决策。如果 Alice 获胜，返回 true ；如果 Bob 获胜，返回 false 。

"""
from collections import Counter
from typing import List


def stoneGameIX(stones: List[int]) -> bool:
    """
    模拟Alice获胜情况，先取1 or 2
    获胜条件：cnt[0]%2==0 and cnt[1]*cnt[2]>1
    cnt[1]%2==1 and abs(cnt[1]-cnt[2])>=3
    :param stones:
    :return:
    """
    cntDict = Counter([v % 3 for v in stones])
    return (cntDict[0] % 2 == 0 and cntDict[1] * cntDict[2] > 0) or (
            cntDict[0] % 2 == 1 and abs(cntDict[1] - cntDict[2]) >= 3)


"""
2030. 含特定字母的最小子序列
给你一个字符串 s ，一个整数 k ，一个字母 letter 以及另一个整数 repetition 。

返回 s 中长度为 k 且 字典序最小 的子序列，该子序列同时应满足字母 letter 出现 至少 repetition 次。生成的测试用例满足 letter 
在 s 中出现 至少 repetition 次。

子序列 是由原字符串删除一些（或不删除）字符且不改变剩余字符顺序得到的剩余字符串。

字符串 a 字典序比字符串 b 小的定义为：在 a 和 b 出现不同字符的第一个位置上，字符串 a 的字符在字母表中的顺序早于字符串 b 的字符。

"""

from collections import deque


def smallestSubsequence(s: str, k: int, letter: str, repetition: int) -> str:
    """
    如果没有reptition个letter，经典问题：algo-improve/0x11-monotoStack.py
    :param s:
    :param k:
    :param letter:
    :param repetition:
    :return:
    """
    stack = deque()
    letterCnts = s.count(letter)
    n = len(s)
    p = 0
    delCnt = n - k
    for i in range(n):
        while stack and delCnt > 0 and stack[-1] > s[i]:
            if stack[-1] == letter:
                if repetition > letterCnts + p - 1:
                    break
                p -= 1
            stack.pop()
            delCnt -= 1

        stack.append(s[i])
        if s[i] == letter:
            p += 1
            letterCnts -= 1
    while len(stack) > k:
        if stack[-1] == letter:
            p -= 1
        stack.pop()
    res = list(stack)
    for i in range(k - 1, -1, -1):
        if p < repetition and res[i] != letter:
            res[i] = letter
            p += 1
    return "".join(res)


if __name__ == "__main__":
    stones = [5, 1, 2, 4, 3]
    print(stoneGameIX(stones))

    s = "leet"
    k = 3
    letter = "e"
    repetition = 1
    print(smallestSubsequence(s, k, letter, repetition))

    s = "leetcode"
    k = 4
    letter = "e"
    repetition = 2
    print(smallestSubsequence(s, k, letter, repetition))
