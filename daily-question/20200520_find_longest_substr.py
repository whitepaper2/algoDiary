#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 下午7:50
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200520_find_longest_substr.py
# @Software: PyCharm


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        note: 请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次
        :param s:
        :return:
        """
        ans, status, n = 0, 0, len(s)
        pos = [-1] * (1 << 5)
        pos[0] = 0

        for i in range(n):
            if s[i] == 'a':
                status ^= 1 << 0
            elif s[i] == 'e':
                status ^= 1 << 1
            elif s[i] == 'i':
                status ^= 1 << 2
            elif s[i] == 'o':
                status ^= 1 << 3
            elif s[i] == 'u':
                status ^= 1 << 4
            if pos[status] != -1:
                ans = max(ans, i + 1 - pos[status])
            else:
                pos[status] = i + 1
        return ans


if __name__ == "__main__":
    s = "eleetminicoworoep"
    ss = Solution()
    print(ss.findTheLongestSubstring(s))  # 13
