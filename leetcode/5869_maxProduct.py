#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 下午1:05
# @Author  : pengyuan.li
# @Site    : 
# @File    : 5869_maxProduct.py
# @Software: PyCharm

# 258场周赛，求字符串中两不相交子序列的最大乘积回文序列


class Solution:

    def maxProduct(self, s: str) -> int:
        """
        len(s)<=12，可利用遍历法求解
        :param s:
        :return:
        """
        self.res = 0

        def isPladrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        def dfs(s, s1, s2, idx):
            if isPladrome(s1) and isPladrome(s2):
                self.res = max(self.res, len(s1) * len(s2))
            if idx == len(s):
                return
            dfs(s, s1 + s[idx], s2, idx + 1)
            dfs(s, s1, s2 + s[idx], idx + 1)
            dfs(s, s1, s2, idx + 1)

        dfs(s, "", "", 0)
        return self.res


if __name__ == "__main__":
    s = "leetcodecom"
    instanceSol = Solution()
    res = instanceSol.maxProduct(s)
    print(res)
