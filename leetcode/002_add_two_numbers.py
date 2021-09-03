#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 下午11:03
# @Author  : pengyuan.li
# @Site    : 
# @File    : 002_add_two_numbers.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(None)
    temp = head
    is_plus = False
    t1 = l1
    t2 = l2
    while t1 is not None and t2 is not None:
        temp_val = t1.val + t2.val
        if is_plus:
            temp_val = temp_val + 1
        temp.next = ListNode(temp_val % 10)
        is_plus = True if int(temp_val / 10) > 0 else False
        t1 = t1.next
        t2 = t2.next
        temp = temp.next

    while t1 is not None:
        temp_val = t1.val
        if is_plus:
            temp_val = temp_val + 1
        temp.next = ListNode(temp_val % 10)
        is_plus = True if int(temp_val / 10) > 0 else False
        t1 = t1.next
        temp = temp.next

    while t2 is not None:
        temp_val = t2.val
        if is_plus:
            temp_val = temp_val + 1
        temp.next = ListNode(temp_val % 10)
        is_plus = True if int(temp_val / 10) > 0 else False
        t2 = t2.next
        temp = temp.next
    if is_plus:
        temp.next = ListNode(1)
    return head.next


if __name__ == "__main__":
    node1 = ListNode(1)
    # node2 = ListNode(4)
    # node4 = ListNode(3)
    # node1.next = node2
    # node2.next = node4
    # temp = node1
    # print(type(temp))
    # while temp is not None:
    #     print(temp.val)
    #     temp = temp.next

    node21 = ListNode(9)
    node23 = ListNode(9)
    # node24 = ListNode(4)
    node21.next = node23
    # node23.next = node24

    out = add_two_numbers(node1, node21)
    while out is not None:
        print(out.val)
        out = out.next
