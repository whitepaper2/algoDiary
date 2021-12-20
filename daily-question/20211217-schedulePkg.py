#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/17 下午2:59
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20211217-schedulePkg.py
# @Software: PyCharm


# import schedule
# import time
# from datetime import datetime, timedelta
#
#
# def job():
#     print("I'm working...")
#
#
# schedule.every(5).seconds.do(job)
# # schedule.every(10).minutes.do(job)
# # schedule.every().hour.do(job)
# # schedule.every().day.at("10:30").do(job)
# # schedule.every(5).to(10).minutes.do(job)
# # schedule.every().monday.do(job)
# # schedule.every().wednesday.at("13:15").do(job)
# # schedule.every().minute.at(":17").do(job)
# yesterday = datetime.now() + timedelta(days=-1)
# pdate = yesterday.strftime('%Y%m%d')
# print(pdate)
# while True:
#     schedule.run_pending()
# time.sleep(1)
import bisect
arr=[12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
k=1
n = len(arr)
cnts = 0
i = 0
while i < k:
    j = i
    f = []
    lens = 0
    while j < n:
        lens += 1
        idx = bisect.bisect_right(f, arr[j])
        if idx == len(f):
            f.append(arr[j])
        else:
            f[idx] = arr[j]
        j += k
    cnts += lens-len(f)
    i += 1

print(cnts)
