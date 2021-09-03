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


def neighbor(curStrs):
    """

    :param curStrs: 0000
    :return: 0001\0010\...\9000
    """
    prev = list()
    last = list()
    for i in range(len(curStrs)):
        istr = curStrs[i]
        if istr == '0':
            prev.append(curStrs[:i] + '9' + curStrs[i + 1:])
        else:
            prev.append(curStrs[:i] + str(int(istr) - 1) + curStrs[i + 1:])
        if istr == '9':
            last.append(curStrs[:i] + '0' + curStrs[i + 1:])
        else:
            last.append(curStrs[:i] + str(int(istr) + 1) + curStrs[i + 1:])
    return prev + last


from collections import deque


def openlock(deadends, target):
    if "0000" in deadends:
        return -1

    lockDict = set()
    lockDict.add("0000")
    queue = deque()
    queue.append(("0000", 0))
    while queue:
        cur, step = queue.popleft()
        neig = neighbor(cur)
        for ele in neig:
            if ele not in lockDict and ele not in deadends:
                if ele == target:
                    return step + 1
                queue.append((ele, step + 1))
                lockDict.add(ele)


def num_prev(x: str) -> str:
    return "9" if x == "0" else str(int(x) - 1)


def num_succ(x: str) -> str:
    return "0" if x == "9" else str(int(x) + 1)


from typing import Generator


# 枚举 status 通过一次旋转得到的数字
def get(status: str) -> Generator[str, None, None]:
    s = list(status)
    for i in range(4):
        num = s[i]
        s[i] = num_prev(num)
        yield "".join(s)
        s[i] = num_succ(num)
        yield "".join(s)
        s[i] = num


def removeOccurrences(s: str, part: str) -> str:
    def removeEle(A, part):
        m = len(part)
        for i in range(len(A)):
            if A[i] == part[0] and A[i:i + m] == part:
                return A[:i] + A[i + m:]
        return A

    cur = s
    while cur:
        others = removeEle(cur, part)
        if others == cur:
            break
        cur = others
        # print(cur)

    return cur


def matMultiply(A, B):
    m = len(A)
    p = len(A[0])
    n = len(B[0])
    C = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            cur = 0
            for k in range(p):
                cur += A[i][k] * B[k][j]
            C[i][j] = cur
    return C



def ntimesMul(A, n):
    if n == 1:
        return A
    n2 = n // 2
    B = ntimesMul(A, n2)
    C = matMultiply(B, B)
    if n % 2 == 1:
        C = matMultiply(A, C)
    return C


if __name__ == "__main__":
    # print(neighbor("0010"))
    # print(removeOccurrences("eemckxmckx","emckx"))
    # print(removeOccurrences("daabcbaabcbc", "abc"))
    # print(removeOccurrences("daabcbaabcbc", "abc"))
    # A = [[0, 0, 1], [0, 0, 0], [0, 1, 0]]
    # A = [[0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [1, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
    # A2 = matMultiply(A, A)
    # A3 = matMultiply(A2, A)
    # A4 = matMultiply(A3, A)
    # A5 = matMultiply(A4, A)
    # print(A2)
    # print(A3)
    # print(A4)
    # print(A5)
    # print(ntimesMul(A, 3))
    for i in range(10):
        print(i)