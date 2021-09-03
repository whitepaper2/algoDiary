#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 下午4:39
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200628_min_subarray_len.py
# @Software: PyCharm
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        note:给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
        :param s:
        :param nums:
        :return:
        """
        nums_len = len(nums)
        min_sublen = nums_len + 1
        subnums_sum = [[0 for _ in range(nums_len)] for _ in range(nums_len)]
        for i in range(nums_len - 1, -1, -1):
            for j in range(nums_len - 1, i - 1, -1):
                if i == j:
                    subnums_sum[i][i] = nums[i]
                else:
                    subnums_sum[i][j] = subnums_sum[i + 1][j] + nums[i]
                if subnums_sum[i][j] >= s and j - i + 1 < min_sublen:
                    min_sublen = j - i + 1
        if min_sublen >= nums_len + 1:
            return 0
        else:
            return min_sublen

    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        """
        note:给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
        双指针法
        :param s:
        :param nums:
        :return:
        """

        nums_len = len(nums)
        min_sublen = nums_len + 1
        start = 0
        end = 0
        subnums_sum = 0
        while end < nums_len:
            subnums_sum += nums[end]
            while subnums_sum >= s:
                min_sublen = min(min_sublen, end - start + 1)
                subnums_sum -= nums[start]
                start = start + 1
            end = end + 1

        return 0 if min_sublen == nums_len + 1 else min_sublen

    def minSubArrayLen3(self, s: int, nums: List[int]) -> int:
        """
        note:给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
        前缀和+二分查找
        :param s:
        :param nums:
        :return:
        """
        import bisect
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        print(sums)
        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans


if __name__ == "__main__":
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    ss = Solution()
    print(ss.minSubArrayLen3(s, nums))
    s = 3
    nums = [1, 1]
    print(ss.minSubArrayLen2(s, nums))
