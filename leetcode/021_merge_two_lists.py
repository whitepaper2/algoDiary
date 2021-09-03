#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 下午11:56
# @Author  : pengyuan.li
# @Site    : 
# @File    : 021_merge_two_lists.py
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    temp_l1 = l1
    temp_l2 = l2
    out = ListNode(None)
    temp_out = out
    while temp_l1 is not None and temp_l2 is not None:
        if temp_l1.val <= temp_l2.val:
            temp_out.next = temp_l1
            temp_l1 = temp_l1.next
        else:
            temp_out.next = temp_l2
            temp_l2 = temp_l2.next
        temp_out = temp_out.next
    if temp_l1 is None:
        while temp_l2 is not None:
            temp_out.next = temp_l2
            temp_l2 = temp_l2.next
            temp_out = temp_out.next
    if temp_l2 is None:
        while temp_l1 is not None:
            temp_out.next = temp_l1
            temp_l1 = temp_l1.next
            temp_out = temp_out.next
    return out.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node4
    temp = node1
    print(type(temp))
    # while temp is not None:
    #     print(temp.val)
    #     temp = temp.next

    node21 = ListNode(1)
    node23 = ListNode(3)
    node24 = ListNode(4)
    node21.next = node23
    node23.next = node24

    out = merge_two_lists(node1, node21)
    while out is not None:
        print(out.val)
        out = out.next
