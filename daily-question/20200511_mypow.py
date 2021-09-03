#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 下午7:41
# @Author  : pengyuan.li
# @Site    : 
# @File    : daily_question/20200511_mypow.py
# @Software: PyCharm


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        n_is_negative = False
        num = n
        if n < 0:
            n_is_negative = True
            num = -n
        res = self.positive_mypow(x, num)
        if n_is_negative:
            res = 1 / res
        return res

    def positive_mypow(self, x, n) -> float:
        if n <= 1:
            return x
        # 重复计算 positive_mypow(x, n // 2)，改为一次节省时间
        # if n % 2 == 0:
        #     return self.positive_mypow(x, n // 2) * self.positive_mypow(x, n // 2)
        # else:
        #     return self.positive_mypow(x, n // 2) * self.positive_mypow(x, n // 2) * x
        half = self.positive_mypow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


if __name__ == "__main__":
    x = 2.0
    n = -5
    ss = Solution()
    print(ss.myPow(x, n))
    # print(positive_mypow(x, n))
    # print(myPow(x, n))
