#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 上午10:12
# @Author  : pengyuan.li
# @Site    : 
# @File    : week266.py
# @Software: PyCharm

"""
2073. 买票需要的时间
有 n 个人前来排队买票，其中第 0 人站在队伍 最前方 ，第 (n - 1) 人站在队伍 最后方 。
给你一个下标从 0 开始的整数数组 tickets ，数组长度为 n ，其中第 i 人想要购买的票数为 tickets[i] 。
每个人买票都需要用掉 恰好 1 秒 。一个人 一次只能买一张票 ，如果需要购买更多票，他必须走到  队尾 重新排队（瞬间 发生，不计时间）。
如果一个人没有剩下需要买的票，那他将会 离开 队伍。
返回位于位置 k（下标从 0 开始）的人完成买票需要的时间（以秒为单位）。
"""
from typing import List, Optional


def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    """
    颇受打击，想的是模拟法求解
    :param tickets:
    :param k:
    :return:
    """
    res = 0
    for i, v in enumerate(tickets):
        if i <= k:
            res += min(tickets[i], tickets[k])
        else:
            res += min(tickets[i], tickets[k] - 1)
    return res


"""
2074. 反转偶数长度组的节点
给你一个链表的头节点 head 。
链表中的节点 按顺序 划分成若干 非空 组，这些非空组的长度构成一个自然数序列（1, 2, 3, 4, ...）。一个组的 长度 就是组中分配到的节点数目。换句话说：
节点 1 分配给第一组
节点 2 和 3 分配给第二组
节点 4、5 和 6 分配给第三组，以此类推
注意，最后一组的长度可能小于或者等于 1 + 倒数第二组的长度 。
反转 每个 偶数 长度组中的节点，并返回修改后链表的头节点 head 。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import math


def reverseEvenLengthGroups(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    没有考虑  @todo 最后一组的长度可能小于或者等于 1 + 倒数第二组的长度
    :param head:
    :return:
    """
    valList = []
    while head:
        valList.append(head.val)
        head = head.next
    n = len(valList)
    group = int(math.sqrt(n))
    rangeLeft = [0] * (group + 1)
    rangeRight = [0] * (group + 1)
    for i in range(1, group + 1):
        rangeLeft[i] = i * (i - 1) // 2 + 1
        rangeRight[i] = i * (i - 1) // 2 + i
    if rangeRight[group] < n:
        group += 1
        rangeLeft.append(min(rangeRight[group - 1] + 1, n))
        rangeRight.append(n)

    def reverseList(l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    valList.insert(0, 0)
    for i in range(1, group + 1):
        if i % 2 == 0:
            reverseList(rangeLeft[i], rangeRight[i], valList)
    print(rangeRight[group]-rangeLeft[group]+1)
    if group%2==1 and (rangeRight[group]-rangeLeft[group]+1)%2==0:
        reverseList(rangeLeft[group], rangeRight[group], valList)
    nodeList = [ListNode(v) for v in valList]
    for i in range(len(nodeList)-1):
        nodeList[i].next = nodeList[i+1]
    return nodeList[0].next


if __name__ == "__main__":
    tickets = [2, 3, 2]
    k = 2
    print(timeRequiredToBuy(tickets, k))

    # head = [5, 2, 6, 3, 9, 1, 7, 3, 8, 4]
    head = [0,4,2,1,3]
    # [5, 6, 2, 3, 9, 1, 4, 8, 3, 7]
    dummy = ListNode()
    nodeLists = []
    for e in head:
        nodeLists.append(ListNode(e))
    for i in range(len(nodeLists) - 1):
        nodeLists[i].next = nodeLists[i + 1]

    reverseHead = reverseEvenLengthGroups(nodeLists[0])
    while reverseHead:
        print(reverseHead.val)
        reverseHead = reverseHead.next
