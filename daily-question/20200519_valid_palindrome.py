#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 上午10:14
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200519_valid_palindrome.py
# @Software: PyCharm


class Solution:
    # 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
    def validPalindrome(self, s: str) -> bool:
        len_s = len(s)
        left = 0
        right = len_s - 1
        while left < right and s[left] == s[right]:
            left = left + 1
            right = right - 1
        return self.Palindrome(s, left + 1, right) or self.Palindrome(s, left, right - 1)

    def Palindrome(self, s: str, i: int, j: int) -> bool:
        """
        note: 双指针法判断是否为回文串
        :param s:
        :param i: start point
        :param j: end point
        :return:
        """
        while i < j and s[i] == s[j]:
            i = i + 1
            j = j - 1
        return i >= j


if __name__ == "__main__":
    ss = Solution()
    s = "aba"
    print(ss.validPalindrome(s))
    s = "abca"
    print(ss.validPalindrome(s))
