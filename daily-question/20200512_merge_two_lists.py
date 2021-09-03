#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 下午5:48
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20200512_merge_two_lists.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        note：两个有序链表，组成一个有序链表，返回head。
        尝试 递归法.数组的思路
        if l1[i].val<l2[j].val, then l1[i]+mergeTwoLists(l1[i+1:],l2[j:])
        else , then l2[j]+mergeTwoLists(l1[i:],l2[j+1:])
        指针：if l1.val < l2.val, then l1.next = mergeTwoLists(l1.next, l2)
        :param l1:
        :param l2:
        :return:
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


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
    nums1 = [1, 2, 4]
    nums2 = [1, 3, 5]
    nums1_head = create_node_list(nums1)
    nums2_head = create_node_list(nums2)
    ss = Solution()
    merge_head = ss.mergeTwoLists(nums1_head, nums2_head)
    while merge_head is not None:
        print(merge_head.val)
        merge_head = merge_head.next
