#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 下午2:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 005_longest_palindrome_substring.py
# @Software: PyCharm


def longest_palindrome(s):
    """
    note: Time Limit Exceeded，循环遍历s[i:j]是否为回文字符串
    :type s: str
    :rtype: str
    """

    def is_palindrome(ss, i, j):
        out = True
        x_str = str(ss[i:j])
        left = 0
        right = len(x_str) - 1
        while left < right:
            if x_str[left] == x_str[right]:
                left = left + 1
                right = right - 1
            else:
                out = False
                break
        return out

    res_len = 0
    res_i = 0
    res_j = 0
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s, i, j) and j - i > res_len:
                res_len = j - i
                res_i = i
                res_j = j
    return s[res_i:res_j]


def longest_palindrome2(s):
    """
    note: 动态规划求回文字符串
    :type s: str
    :rtype: str
    """
    res_left = 0
    res_right = 0
    res_len = 0
    dp = []
    for j in range(len(s)):
        dp.append([0] * len(s))
        dp[j][j] = 1
        for i in range(0, j):
            # if j - i > 1:
            #     dp[i][j] = 1 if s[i] == s[j] and dp[i + 1][j - 1] else 0
            # else:
            #     dp[i][j] = 1 if s[i] == s[j] else 0
            dp[i][j] = 1 if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]) else 0
            if dp[i][j] and res_len < j - i + 1:
                res_len = j - i + 1
                res_left = i
                res_right = j

    return s[res_left:res_right + 1]


def longest_palindrome3(s):
    """
    note: 一段字符的求回文字符串
    :type s: str
    :rtype: str
    """
    n = len(s)
    if n < 2:
        return s
    start = 0
    max_len = 0
    i = 0
    while i < n:
        if n - i <= max_len // 2:
            break
        left = i
        right = i
        while right < n - 1 and s[right + 1] == s[right]:
            right = right + 1
        i = right + 1
        while right < n - 1 and left > 0 and s[right + 1] == s[left - 1]:
            right = right + 1
            left = left - 1
        if max_len < right - left + 1:
            max_len = right - left + 1
            start = left

    return s[start:start + max_len]


def longest_palindrome4(s):
    """
    note: O(n)时间求回文字符串，还没完成。
    :type s: str
    :rtype: str
    """
    res_left = 0
    res_right = 0
    res_len = 0
    dp = []
    for j in range(len(s)):
        dp.append([0] * len(s))
        dp[j][j] = 1
        for i in range(0, j):
            # if j - i > 1:
            #     dp[i][j] = 1 if s[i] == s[j] and dp[i + 1][j - 1] else 0
            # else:
            #     dp[i][j] = 1 if s[i] == s[j] else 0
            dp[i][j] = 1 if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]) else 0
            if dp[i][j] and res_len < j - i + 1:
                res_len = j - i + 1
                res_left = i
                res_right = j

    return s[res_left:res_right + 1]


if __name__ == "__main__":
    s = "babad"
    print(longest_palindrome3(s))

    s = "cbbd"
    print(longest_palindrome3(s))

    s = ""
    print(longest_palindrome3(s))
