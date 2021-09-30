#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 下午1:05
# @Author  : pengyuan.li
# @Site    : 
# @File    : 5869_maxProduct.py
# @Software: PyCharm

"""
258场周赛，求字符串中两不相交子序列的最大乘积回文序列
"""


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

    def maxProduct2(self, s: str) -> int:
        n = len(s)
        total = []  # 存放所有回文子序列
        for i in range(1, 1 << n):  # 用位运算列出所有子序列
            temp = ''
            for j in range(n):
                if (1 << j) & i:
                    temp += s[j]
            if temp == temp[::-1]:  # 判断是否为回文
                total.append(i)

        def count1(m: int):  # 统计二进制中1的个数
            res = 0
            while m:
                res += (m & 1)
                m >>= 1
            return res

        ret = 0
        for i in range(len(total)):
            for j in range(i + 1, len(total)):
                if total[i] & total[j] == 0:  # total[i]&total[j]为0说明俩子序列不相交
                    ret = max(ret, count1(total[i]) * count1(total[j]))
        return ret  # 1的个数表示回文序列的长度，并计算俩长度的乘积

    def maxProduct3(self, s: str) -> int:
        n = len(s)
        total = []  # 存放所有回文子序列
        for i in range(1, 1 << n):  # 用位运算列出所有子序列
            temp = ''
            for j in range(n):
                if (1 << j) & i:
                    temp += s[j]
            if temp == temp[::-1]:  # 判断是否为回文
                total.append((i, len(temp)))

        ret = 0
        for i in range(len(total)):
            kx, x = total[i]
            for j in range(i + 1, len(total)):
                ky, y = total[j]
                if kx & ky:
                    continue
                ret = max(ret, x * y)
        return ret


if __name__ == "__main__":
    s = "leetcodecom"
    instanceSol = Solution()
    print(instanceSol.maxProduct(s))
    print(instanceSol.maxProduct2(s))
    print(instanceSol.maxProduct3(s))
