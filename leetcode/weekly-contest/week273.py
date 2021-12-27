#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 上午10:12
# @Author  : pengyuan.li
# @Site    : 
# @File    : week273.py
# @Software: PyCharm


"""
5966. 还原原数组
Alice 有一个下标从 0 开始的数组 arr ，由 n 个正整数组成。她会选择一个任意的 正整数 k 并按下述方式创建两个下标从 0 开始的新整数数组 lower 和 higher ：

对每个满足 0 <= i < n 的下标 i ，lower[i] = arr[i] - k
对每个满足 0 <= i < n 的下标 i ，higher[i] = arr[i] + k
不幸地是，Alice 丢失了全部三个数组。但是，她记住了在数组 lower 和 higher 中出现的整数，但不知道每个整数属于哪个数组。请你帮助 Alice 还原原数组。

给你一个由 2n 个整数组成的整数数组 nums ，其中 恰好 n 个整数出现在 lower ，剩下的出现在 higher ，还原并返回 原数组 arr 。如果出现答案不唯一的情况，返回 任一 有效数组。

注意：生成的测试用例保证存在 至少一个 有效数组 arr 。
"""
from typing import List


def recoverArray(nums: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)

    def _check(k2, right):
        left = 0
        while right < n:
            if nums[right] - nums[left] == k2:
                nums[right] *= -1
                left += 1
                right += 1
                while left < n and nums[left] < 0:
                    nums[left] *= -1
                    left += 1
            else:
                right += 1
        i = left
        while i < right:
            if nums[i] < 0:
                nums[i] *= -1

            i += 1

        return left == n

    def _getResult(k2, right):
        res = []
        k = k2 // 2
        left = 0
        while right < n:
            if nums[right] - nums[left] == k2:
                res.append(nums[left] + k)
                nums[right] *= -1
                left += 1
                right += 1
                while left < n and nums[left] < 0:
                    left += 1
            else:
                right += 1
        return res

    for i in range(1, n):
        t = nums[i] - nums[0]  # t=2*k
        if t & 1:
            continue
        if t == 0:
            continue
        if _check(t, i):
            return _getResult(t, i)


if __name__ == "__main__":
    nums = [2, 10, 6, 4, 8, 12]
    print(recoverArray(nums))
