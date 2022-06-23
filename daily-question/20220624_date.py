#!/usr/bin/env python
# -*- coding: utf-8 -*-

# here put the import lib
""" 
一、解题思路
订单到期是由订单周期决定的，由例子”在 2019-01-30 订购一个月，订购将在 2019-02-28 过期“可知，一月周期不会跨2个月份
2月最后一天，共有12个,比如2019年2月28日到期
一个月周期：2019-1-28,2019-1-29，2019-1-30,2019-1-31
一季度周期：2018-11-28,2018-11-29,2018-11-30
半年周期：2018-8-28,2018-8-29,2018-8-30,2018-8-31
一年周期：2018-2-28 
"""
""" 
二、解题思路
1、判断是否为闰年
2、月份分是否跨年
3、一个月周期选定标准是天数+月周期求余，月底特殊处理 
"""


def getExpirationDate(year, month, day):
    # TODO
    if not str(year).isdigit():
        raise Exception("The input year not int!")
    # 是否闰年
    def isLeap(year):
        res = False
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    res = True
            else:
                res = True
        return res

    month2days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isLeap(year):
        month2days[2] = 29
    # 输入是否合法
    def checkMD(month, day):
        return str(month).isdigit() and 0 < month <= 12 and str(
            day).isdigit() and 0 < day <= month2days[month]

    if not checkMD(month, day):
        raise Exception("The input month or day may not correct!")

    if month < 12:
        month += 1
        if day >= month2days[month]:
            day = month2days[month]
        else:
            day = (day + month2days[month]) % month2days[month]
    else:
        month = 1
        year += 1
        day = (day + month2days[month]) % month2days[month]

    return [year, month, day]


if __name__ == "__main__":
    assert getExpirationDate(2019, 1, 28) == [2019, 2, 28]
    assert getExpirationDate(2019, 1, 30) == [2019, 2, 28]

    print(getExpirationDate(2019, 1, 31))
    assert getExpirationDate(2019, 5, 31) == [2019, 6, 30]
    assert getExpirationDate(2019, 2, 20) == [2019, 3, 20]
    print(getExpirationDate(2018, 11, 10))
    print(getExpirationDate(2019, 4, 30))
    assert getExpirationDate(2018, 1, 1) == [2018, 2, 1]
    assert getExpirationDate(2019, 12, 10) == [2020, 1, 10]
