#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/06/23 14:47:26
@Author  : pengyuan.li
@File    : 20220624_date.py
@Software: VSCode
'''

# here put the import lib
# 1、服务器是自建机房还是买的阿里云、华为云？
# 2、公司做营销服务淘宝中小客户，不是应该有数据分析人员吗？感觉找的都是功能开发人员，上线某个功能是谁来拍板的？难道只是堆功能
# 转开发原因：1、算法岗位要求发论文；投入大产出少；研发岗位比较实用，比如开发小程序；不论开发或数据挖掘，都是工具，主要能产生价值
# web开发：


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


def getExpirationDate2(year, month, day, n):
    """
    n:周期，1、2、3、6、12
    """
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

    month2days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isLeap(year):
        month2days[1] = 29
    # 输入是否合法
    def checkMD(month, day):
        return str(month).isdigit() and 0 < month <= 12 and str(
            day).isdigit() and 0 < day <= month2days[month - 1]

    if not checkMD(month, day):
        raise Exception("The input month or day may not correct!")

    incyear = (month + n - 1) // 12
    incmonth = (month + n - 1) % 12
    year += incyear
    month = incmonth + 1
    if day >= month2days[incmonth]:
        day = month2days[incmonth]
    else:
        day = (day + month2days[incmonth]) % month2days[incmonth]

    return [year, month, day]


def getDurationDays(year, month, day, n):
    _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    _DAYS_BEFORE_MONTH = [-1]  # -1 is a placeholder for indexing purposes.
    dbm = 0
    for dim in _DAYS_IN_MONTH[1:]:
        _DAYS_BEFORE_MONTH.append(dbm)
        dbm += dim
    del dbm, dim

    def _is_leap(year):
        "year -> 1 if leap year, else 0."
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def _days_before_year(year):
        "year -> number of days before January 1st of year."
        y = year - 1
        return y * 365 + y // 4 - y // 100 + y // 400

    def _days_in_month(year, month):
        "year, month -> number of days in that month in that year."
        assert 1 <= month <= 12, month
        if month == 2 and _is_leap(year):
            return 29
        return _DAYS_IN_MONTH[month]

    def _days_before_month(year, month):
        "year, month -> number of days in year preceding first day of month."
        assert 1 <= month <= 12, 'month must be in 1..12'
        return _DAYS_BEFORE_MONTH[month] + (month > 2 and _is_leap(year))

    def _ymd2ord(year, month, day):
        "year, month, day -> ordinal, considering 01-Jan-0001 as day 1."
        assert 1 <= month <= 12, 'month must be in 1..12'
        dim = _days_in_month(year, month)
        assert 1 <= day <= dim, ('day must be in 1..%d' % dim)
        return (_days_before_year(year) + _days_before_month(year, month) +
                day)

    startDate2ord = _ymd2ord(year, month, day)
    expiryear, expirmonth, expirday = getExpirationDate2(year, month, day, n)
    endDate2ord = _ymd2ord(expiryear, expirmonth, expirday)
    return endDate2ord - startDate2ord


if __name__ == "__main__":

    print(getDurationDays(2019, 1, 28,14))
    assert getExpirationDate(2019, 1, 28) == [2019, 2, 28]
    assert getExpirationDate(2019, 1, 30) == [2019, 2, 28]

    print(getExpirationDate2(2019, 1, 31, 1))
    assert getExpirationDate(2019, 5, 31) == [2019, 6, 30]
    assert getExpirationDate(2019, 2, 20) == [2019, 3, 20]
    print(getExpirationDate(2018, 11, 10))
    print(getExpirationDate(2019, 4, 30))
    assert getExpirationDate(2018, 1, 1) == [2018, 2, 1]
    assert getExpirationDate(2019, 12, 10) == [2020, 1, 10]

# 解题思路
# 1、判断是否为闰年
# 2、月份分是否跨年
# 3、一个月周期选定标准是天数+月周期求余，月底特殊处理
