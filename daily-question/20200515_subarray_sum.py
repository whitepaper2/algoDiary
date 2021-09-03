#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 下午10:43
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200515_subarray_sum.py
# @Software: PyCharm

from typing import List


# 数组中连续子数组之和=k的个数
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        note：暴力求解
        :param nums:
        :param k:
        :return:
        """
        cnt = 0
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, -1, -1):
                cur_sum += nums[j]
                if cur_sum == k:
                    cnt = cnt + 1
        return cnt

    def subarraySum2(self, nums: List[int], k: int) -> int:
        """
        note：sum([j,...,i]=k, pre[i]=sum([0,...,i]) , pre[i]-pre[j-1]=k
        :param nums:
        :param k:
        :return:
        """
        cnt = 0
        sum_dict = {0: 1}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if sum_dict.get(cur_sum - k):
                cnt += sum_dict.get(cur_sum - k)
            sum_dict[cur_sum] = sum_dict.setdefault(cur_sum, 0) + 1
        return cnt


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    ss = Solution()
    print(ss.subarraySum2(nums, k))
