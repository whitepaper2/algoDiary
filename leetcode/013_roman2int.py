#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 下午3:01
# @Author  : pengyuan.li
# @Site    : 
# @File    : 013_roman2int.py
# @Software: PyCharm


def roman2int(s):
    """
    :type s: str
    :rtype: int
    """
    out = 0
    user_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    user_dict2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    len_s = len(s)
    i = 0
    while i < len_s:
        if s[i] == "I" and i + 1 != len_s and s[i + 1] == "V":
            out = out + 4
            i = i + 2
            continue
        elif s[i] == "I" and i + 1 != len_s and s[i + 1] == "X":
            out = out + 9
            i = i + 2
            continue
        elif s[i] == "X" and i + 1 != len_s and s[i + 1] == "L":
            out = out + 40
            i = i + 2
            continue
        elif s[i] == "X" and i + 1 != len_s and s[i + 1] == "C":
            out = out + 90
            i = i + 2
            continue
        elif s[i] == "C" and i + 1 != len_s and s[i + 1] == "D":
            out = out + 400
            i = i + 2
            continue
        elif s[i] == "C" and i + 1 != len_s and s[i + 1] == "M":
            out = out + 900
            i = i + 2
            continue
        else:
            out = out + user_dict[s[i]]
            i = i + 1
    return out


def roman2int2(s):
    """
    :type s: str
    :rtype: int
    """
    str_s = []
    user_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                 "CD": 400, "CM": 900}
    len_s = len(s)
    i = 0
    while i < len_s:
        if s[i] == "I" and i + 1 != len_s and s[i + 1] == "V":
            str_s.append("IV")
            i = i + 2
            continue
        elif s[i] == "I" and i + 1 != len_s and s[i + 1] == "X":
            str_s.append("IX")
            i = i + 2
            continue
        elif s[i] == "X" and i + 1 != len_s and s[i + 1] == "L":
            str_s.append("XL")
            i = i + 2
            continue
        elif s[i] == "X" and i + 1 != len_s and s[i + 1] == "C":
            str_s.append("XC")
            i = i + 2
            continue
        elif s[i] == "C" and i + 1 != len_s and s[i + 1] == "D":
            str_s.append("CD")
            i = i + 2
            continue
        elif s[i] == "C" and i + 1 != len_s and s[i + 1] == "M":
            str_s.append("CM")
            i = i + 2
            continue
        else:
            str_s.append(s[i])
            i = i + 1
    out = sum([user_dict[i] for i in str_s])
    return out


if __name__ == "__main__":
    """
    method2 is so faster than method1
    """
    print(roman2int2("III"))
    print(roman2int2("IV"))
    print(roman2int2("IX"))
    print(roman2int2("LVIII"))
    print(roman2int2("MCMXCIV"))
