#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 下午3:11
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20210926_snow.py
# @Software: PyCharm


def getMaxPath(grid):
    """
    第260场周赛，网格游戏
    """
    c = len(grid[0])

    left = 0
    right = 0
    for i in range(1, c):
        right += grid[0][i]
    maxPath = right
    for i in range(1, c):
        left += grid[1][i - 1]
        right -= grid[0][i]
        maxPath = min(maxPath, max(left, right))
    return maxPath


def printPos(a, b):
    """
    计算偏移，约瑟夫环，《算法进阶》hash，判断6边型是否相等。
    :param a:
    :param b:
    :return:
    """
    n = len(a)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(a[(i + k) % n], b[(j + k) % n])


from typing import List


def placeWordInCrossword(board: List[List[str]], word: str) -> bool:
    """
    四种状态，board(正、反)+word(正、反)
    :param board:
    :param word:
    :return:
    """

    def check(board, word):
        """
        记录可选的左边界，再判断是否与单词匹配
        :param board:
        :param word:
        :return:
        """
        m = len(board)
        n = len(board[0])
        k = len(word)
        for i in range(m):
            acc = [0] * n
            for j in range(n - 1, -1, -1):
                if board[i][j] == "#":
                    acc[j] = 0
                else:
                    acc[j] = 1 if j == n - 1 else acc[j + 1] + 1
            for j in range(n):
                if acc[j] == k and (j == 0 or board[i][j - 1] == "#"):
                    good = True
                    for p in range(k):
                        if board[i][j + p] != word[p] and board[i][j + p] != " ":
                            good = False
                            break
                    if good:
                        return True
        return False

    m = len(board)
    n = len(board[0])
    b1 = check(board, word)
    if b1:
        return True

    board2 = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            board2[i][j] = board[j][i]
    b2 = check(board2, word)
    if b2:
        return True
    b3 = check(board, list(reversed(word)))
    if b3:
        return True
    b4 = check(board2, list(reversed(word)))
    return b4


from itertools import product
from collections import Counter
from functools import lru_cache


def scoreOfStudents(s: str, answers: List[int]) -> int:
    @lru_cache(None)
    def helper(s):
        if s.isdigit():
            return {int(s)}
        res = set()
        for i, char in enumerate(s):
            if char == "+":
                res |= {a + b for a, b in product(helper(s[:i]), helper(s[i + 1:])) if a + b < 1000}
            elif char == "*":
                res |= {a * b for a, b in product(helper(s[:i]), helper(s[i + 1:])) if a * b < 1000}

        return res

    ans = helper(s)
    rightAns = eval(s)
    ansCnts = Counter(answers)
    return sum([2 * ansCnts[x] for x in ans]) + 3 * ansCnts[rightAns]


if __name__ == "__main__":
    # grid = [[20, 3, 20, 17, 2, 12, 15, 17, 4, 15], [20, 10, 13, 14, 15, 5, 2, 3, 14, 3]]
    # print(getMaxPath(grid))
    #
    # a = [1, 2, 3, 4, 5, 6]
    # b = [2, 3, 4, 5, 6, 1]
    # printPos(a, b)
    #
    # board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]]
    # word = "abc"
    #
    # board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]]
    # word = "ac"
    #
    # board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]]
    # word = "ca"
    # print(placeWordInCrossword(board, word))
    #
    # board = [[" "], ["#"], ["o"], [" "], ["t"], ["m"], ["o"], [" "], ["#"], [" "]]
    # word = "octmor"
    #
    # print(placeWordInCrossword(board, word))

    s = "6+0*1"
    answers = [12, 9, 6, 4, 8, 6]
    print(scoreOfStudents(s, answers))
