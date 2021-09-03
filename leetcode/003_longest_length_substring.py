#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 下午5:08
# @Author  : pengyuan.li
# @Site    : 
# @File    : 003_longest_length_substring.py
# @Software: PyCharm


def longest_length_substring(s):
    """
    note：Time exceed limited。逐层遍历
    :type s: str
    :rtype: int
    """

    def all_unique(ss, i, j):
        """
        :param ss: 给定的字符串
        :param i: 起始位置
        :param j: 终点位置
        :return: ss(i,j)是唯一子串，返回True; 否则false
        """
        user_set = set()
        for k in range(i, j):
            if ss[k] not in user_set:
                user_set.add(ss[k])
            else:
                return False
        return True

    res = 0
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            if all_unique(s, i, j):
                res = max(res, j - i)
            else:
                break
    return res


def longest_length_substring2(s):
    """
    note: 划窗思想。窗口[i,j)含有s[j],不加入窗口中并且删除窗口中的该元素；否则添加窗口中。只记录最大的窗口大小 j-i
    :type s: str
    :rtype: int
    """
    res = 0
    i = 0
    j = 0
    user_set = set()
    while i < len(s) and j < len(s):
        if s[j] not in user_set:
            user_set.add(s[j])
            j = j + 1
            res = max(res, j - i)
        else:
            user_set.remove(s[i])
            i = i + 1

    return res


def longest_length_substring3(s):
    """
    note：优化划窗思想。窗口[i,j)含有s[j],不加入窗口中并且删除窗口中的该元素；否则添加窗口中。只记录最大的窗口大小j-i
    :type s: str
    :rtype: int
    """
    res = 0
    i = 0
    j = 0
    user_dict = {}
    while i < len(s) and j < len(s):
        if user_dict.get(s[j]) is not None:
            i = max(user_dict.get(s[j]), i)
        res = max(res, j - i + 1)
        user_dict[s[j]] = j + 1
        j = j + 1

    return res


if __name__ == "__main__":
    s = "pwwkew"
    print(longest_length_substring3(s))

    s = "abcabcbb"
    print(longest_length_substring3(s))

    s = "bbbb"
    print(longest_length_substring3(s))

    s = " "
    print(longest_length_substring3(s))
