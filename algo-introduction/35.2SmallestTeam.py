#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 下午8:31
# @Author  : pengyuan.li
# @Site    : 
# @File    : 35.2SmallestTeam.py
# @Software: PyCharm

from typing import List


def smallestSufficientTeam(req_skills: List[str], people: List[List[str]]) -> List[int]:
    # 为skills建立字典
    n = len(req_skills)
    d = dict()
    for i in range(n):
        d[req_skills[i]] = i
    # 所有状态
    dp = [list(range(len(people))) for _ in range(1 << n)]
    dp[0] = []
    # 遍历所有人
    for i in range(len(people)):
        # 求这个人的技能
        skill = 0
        for s in people[i]:
            skill |= (1 << d[s])
        for k, v in enumerate(dp):
            # 把这个人加入进来以后的团队技能
            new_skills = k | skill
            # 如果团队技能因此而增加 并且增加后的人数比新技能原来的人数少 则更新答案
            if new_skills != k and len(dp[new_skills]) > len(v) + 1:
                dp[new_skills] = v + [i]
    return dp[(1 << n) - 1]


if __name__ == "__main__":
    # req_skills = ["java", "nodejs", "reactjs"]
    # people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    # print(smallestSufficientTeam(req_skills, people))

    # n = 10
    # res = list()
    # cur = [x for x in range(2, n + 1)]
    # typeDict = {x: 0 for x in cur}
    # # typeDict[2] = 1
    # while True:
    #     oneVal = [k for k, v in typeDict.items() if v == 0]
    #     if len(oneVal)==0:
    #         break
    #     minPrime = min(oneVal)
    #     res.append(minPrime)
    #     for i in range(2, n + 1):
    #         if i % minPrime == 0:
    #             typeDict[i] = 1
    #     typeDict[minPrime] = 1
    #     # if all(typeDict)==2:
    #     #     break
    #
    #
    # print(res)
    label = 14
    row = 1
    rowStart = 1
    while rowStart*2 <= label:
        row += 1
        rowStart = 2 * rowStart
    print(row, rowStart)
    # row = row-1

    def getReverse(label, row):
        return (1 << row) + (1 << row - 1) - label - 1
    list.sort()

    if row % 2 == 0:
        label = getReverse(label, row)
    path = []
    while row > 0:
        if row % 2 == 0:
            path.append(getReverse(label, row))
        else:
            path.append(label)
        row -= 1
        label >>= 1
    print(path)
