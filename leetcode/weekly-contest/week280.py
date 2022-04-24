#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/02/14 10:05:44
@Author  : pengyuan.li
@File    : week280.py
@Software: VSCode
'''

# here put the import lib
"""
2172. 数组的最大与和

给你一个长度为 n 的整数数组 nums 和一个整数 numSlots ，满足2 * numSlots >= n 。总共有 numSlots 个篮子，编号为 1 到 numSlots 。
你需要把所有 n 个整数分到这些篮子中，且每个篮子 至多 有 2 个整数。一种分配方案的 与和 定义为每个数与它所在篮子编号的 按位与运算 结果之和。
比方说，将数字 [1, 3] 放入篮子 1 中，[4, 6] 放入篮子 2 中，这个方案的与和为 (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4 。
请你返回将 nums 中所有数放入 numSlots 个篮子中的最大与和。
"""
from typing import List


class Solution:

    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        f = [0] * (1 << (numSlots * 2))
        for i, fi in enumerate(f):
            c = bin(i).count('1')  # i.bit_count()
            if c >= len(nums):
                continue
            for j in range(numSlots * 2):
                if (i & (1 << j)) == 0:  # 枚举空篮子 j
                    s = i | (1 << j)
                    f[s] = max(f[s], fi + ((j // 2 + 1) & nums[c]))
        return max(f)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    numSlots = 3
    ss = Solution()
    print(ss.maximumANDSum(nums, numSlots))

    nums = [1, 3, 10, 4, 7, 1]
    numSlots = 9
    print(ss.maximumANDSum(nums, numSlots))