#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 上午9:12
# @Author  : pengyuan.li
# @Site    : 
# @File    : 083_delete_duplicates.py
# @Software: PyCharm
from common import timeit


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


@timeit
def delete_duplicates(head):
    """
    note：有序链表，双指针法。
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return None
    if head.next is None:
        return head
    out = head
    temp_i = head
    temp_j = head.next
    while temp_i is not None and temp_j is not None:
        if temp_i.val != temp_j.val:
            temp_i.next = temp_j
            temp_i = temp_i.next
        temp_j = temp_j.next
    temp_i.next = None
    return out


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node1.next = node2
    node2.next = node3
    out = delete_duplicates(node1)
    temp = out
    while temp is not None:
        print(temp.val)
        temp = temp.next

    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    node6 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    out = delete_duplicates(node1)
    temp = out
    while temp is not None:
        print(temp.val)
        temp = temp.next

