#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 下午2:09
# @Author  : pengyuan.li
# @Site    : 
# @File    : 079_word_exists.py
# @Software: PyCharm

from typing import List


# 深度优先遍历+回溯
def exist(board: List[List[str]], word: str) -> bool:
    m = len(board)
    if m == 0:
        return False
    n = len(board[0])
    is_visited = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if word[0] == board[i][j]:
                is_visited[i][j] = 1
                if backtrack_substr(i, j, board, word[1:], is_visited):
                    return True
                else:
                    is_visited[i][j] = 0

    return False


# 子串是否满足
def backtrack_substr(i, j, board, sub_word, is_visited):
    if len(sub_word) == 0:
        return True
    directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for direct in directs:
        cur_i = i + direct[0]
        cur_j = j + direct[1]
        if 0 <= cur_i < len(board) and 0 <= cur_j < len(board[0]) and board[cur_i][cur_j] == sub_word[0]:
            if is_visited[cur_i][cur_j] == 1:
                continue
            else:
                is_visited[cur_i][cur_j] = 1
                if backtrack_substr(cur_i, cur_j, board, sub_word[1:], is_visited):
                    return True
                else:
                    is_visited[cur_i][cur_j] = 0
    return False


# 深度优先遍历
def exist2(board: List[List[str]], word: str) -> bool:
    m = len(board)
    if m == 0:
        return False
    n = len(board[0])
    is_visited = [[False for _ in range(n)] for _ in range(m)]

    def sub_isexists(board: List[List[str]], word: str, ind: int, i: int, j: int, is_visited: List[List[bool]]) -> bool:
        """
        note: 当前字符能否在二维矩阵中找到
        :param board: 字母的二维矩阵
        :param word: 待匹配的字符串
        :param ind: 第ind个字符
        :param i: 矩阵坐标i
        :param j: 矩阵坐标j
        :param is_visited: 标记是否访问过
        :return: T/F
        """
        if ind == len(word):
            return True
        m = len(board)
        n = len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n or is_visited[i][j] or board[i][j] != word[ind]:
            return False
        is_visited[i][j] = True
        res = sub_isexists(board, word, ind + 1, i + 1, j, is_visited) or sub_isexists(board, word, ind + 1, i - 1, j,
                                                                                       is_visited) \
              or sub_isexists(board, word, ind + 1, i, j + 1, is_visited) or sub_isexists(board, word, ind + 1, i,
                                                                                          j - 1, is_visited)
        is_visited[i][j] = False
        return res

    for i in range(m):
        for j in range(n):
            if sub_isexists(board, word, 0, i, j, is_visited):
                return True
    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(exist2(board, word))
    word = "SEE"
    print(exist(board, word))
    word = "ABCB"
    print(exist2(board, word))
