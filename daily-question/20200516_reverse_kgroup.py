#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 下午5:17
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200516_reverse_kgroup.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        note: k<=len(head)
        :param head:
        :param k:
        :return:
        """

        pass

    def reverse_listnode(self, head: ListNode, tail: ListNode) -> (ListNode, ListNode):
        """
        note: 反转链表
        :param head:
        :param tail:
        :return: (tail, head)
        """
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverse_listnode2(self, head: ListNode) -> ListNode:
        """
        note: 反转链表
        :param head:
        :return:
        """
        null_node = ListNode(0)
        p = head
        while p:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return null_node.next


def create_node_list(nums):
    """
    note: 一组数据组成链表，返回head
    :param nums:
    :return:
    """
    nums_node = []
    for i in range(0, len(nums)):
        nums_node.append(ListNode(nums[i]))
    for i in range(0, len(nums_node) - 1):
        nums_node[i].next = nums_node[i + 1]
    return nums_node[0]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    nums_head = create_node_list(nums)
