#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 下午8:22
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200526_find_duplicate.py
# @Software: PyCharm

from typing import List


class Solution:
    # 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.setdefault(num, 0) + 1
            if nums_dict[num] > 1:
                return num


if __name__ == "__main__":
    ss = Solution()
    nums = [1, 3, 4, 2, 2]
    print(ss.findDuplicate(nums))
