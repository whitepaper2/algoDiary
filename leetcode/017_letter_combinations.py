#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 下午6:22
# @Author  : pengyuan.li
# @Site    : 
# @File    : 017_letter_combinations.py
# @Software: PyCharm


def letter_combinations(digits):
    """
    note: 递归思想
    :type digits: str
    :rtype: List[str]
    """
    number_digit = {"0": "", "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs",
                    "8": "tuv", "9": "wxyz"}
    res = []

    def letter_combinations_dfs(digits, number_digit, depth, cur_res, res):
        if depth == len(digits):
            res.append(cur_res)
        else:
            cur_str = number_digit[digits[depth]]
            for i in range(len(cur_str)):
                letter_combinations_dfs(digits, number_digit, depth + 1, cur_res + cur_str[i], res)

    letter_combinations_dfs(digits, number_digit, 0, "", res)
    return res if len(digits) > 0 else []


if __name__ == "__main__":
    digits = "23"
    print(letter_combinations(digits))
