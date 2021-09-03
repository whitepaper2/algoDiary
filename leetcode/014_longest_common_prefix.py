#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 下午4:02
# @Author  : pengyuan.li
# @Site    : 
# @File    : 014_longest_common_prefix.py
# @Software: PyCharm


def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    len_strs = len(strs)
    out = ""
    if len_strs == 0:
        out = ""
    elif len_strs == 1:
        out = strs[0]
    else:
        min_len = min([len(x) for x in strs])
        for j in range(min_len):
            user_dict = {}
            for i in range(len_strs):
                user_dict[strs[i][j]] = strs[i][j]
            if len(user_dict) == 1:
                out = out + strs[0][j]
            else:
                break
    return out


def longest_common_prefix2(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    len_strs = len(strs)
    if len_strs == 0:
        out = ""
    elif len_strs == 1:
        out = strs[0]
    else:
        out_list = []
        min_len = min([len(x) for x in strs])
        for j in range(min_len):
            user_dict = {}
            for i in range(len_strs):
                user_dict[strs[i][j]] = strs[i][j]
            if len(user_dict) == 1:
                out_list.append(strs[0][j])
            else:
                break
        out = "".join(out_list)
    return out


def longest_common_prefix3(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    len_strs = len(strs)
    out = ""
    if len_strs > 0:
        min_len = min([len(x) for x in strs])
        for j in range(min_len):
            user_dict = {}
            for i in range(len_strs):
                user_dict[strs[i][j]] = strs[i][j]
            if len(user_dict) == 1:
                out = out + strs[0][j]
            else:
                break
    return out


if __name__ == "__main__":
    """
    strs = ["flower","flow","flight"], return "fl"
    strs = ["dog","racecar","car"], return ""
    method1 is so faster than method2
    """
    strs = ["flower", "flow", "flight"]
    print(longest_common_prefix3(strs))
    strs = ["dog", "racecar", "car"]
    print(longest_common_prefix3(strs))
    strs = []
    print(longest_common_prefix3(strs))
    strs = ["dog"]
    print(longest_common_prefix3(strs))
