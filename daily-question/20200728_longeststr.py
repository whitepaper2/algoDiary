#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 下午4:22
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200728_longeststr.py
# @Software: PyCharm

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        c = list(s)
        n = len(c)

        def divide(left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            left_len = divide(left, mid - 1)
            right_len = divide(mid+1, right)
            cur_len = 1
            tmp = list(c[mid])
            i = mid - 1
            while i >= left and c[i] not in tmp:
                tmp.append(c[i])
                i = i - 1
            j = mid + 1
            while j <= right and c[j] not in tmp:
                tmp.append(c[j])
                j = j + 1
            return max(left_len, right_len, len(tmp))

        return divide(0, n - 1)


if __name__ == "__main__":
    s = "abcabcbb"
    ob = Solution()
    print(ob.lengthOfLongestSubstring(s))
