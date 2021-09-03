#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 下午7:47
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200518_max_product.py
# @Software: PyCharm


from typing import List


# 求数组中连续子数组的最大乘积
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = float("-inf")
        n = len(nums)
        p_matrix = [[1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    p_matrix[i][j] = p_matrix[i][j] * nums[j]
                else:
                    p_matrix[i][j] = p_matrix[i][j - 1] * nums[j]
                max_p = max(max_p, p_matrix[i][j])
        return max_p

    def maxProduct2(self, nums: List[int]) -> int:
        """
        note: 以下标i为结尾的最大乘积 max(p[j...i]) = if nums[i]>0, max(p[j...i-1])越大越好 ; if nums[i]<0, min(p[j...i-1])越小越好。
        max(p[j...i]) = max( max(p[j...i-1])*nums[i], nums[i], min(p[j...i-1])*nums[i] )
        min(p[j...i]) = min( max(p[j...i-1])*nums[i], nums[i], min(p[j...i-1])*nums[i] )
        :param nums:
        :return:
        """
        n = len(nums)
        max_p = [nums[0] for _ in range(n)]
        min_p = [nums[0] for _ in range(n)]
        for i in range(1, n):
            max_p[i] = max(max_p[i - 1] * nums[i], nums[i], min_p[i - 1] * nums[i])
            min_p[i] = min(max_p[i - 1] * nums[i], nums[i], min_p[i - 1] * nums[i])
        print(max_p)
        return max(max_p)


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    ss = Solution()
    print(ss.maxProduct(nums))
    print(ss.maxProduct2(nums))
