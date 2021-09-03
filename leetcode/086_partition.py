#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 下午5:24
# @Author  : pengyuan.li
# @Site    : 
# @File    : 086_partition.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x):
    """
    note: 声明一个空的首链表值，使用cur.next遍历，可以同时使用cur,cur.next两值
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    dummy = ListNode(None)
    dummy.next = head
    pre = dummy
    while pre.next is not None and pre.next.val < x:
        pre = pre.next
    cur = pre
    while cur.next is not None:
        if cur.next.val < x:
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
            pre = pre.next
        else:
            cur = cur.next
    return dummy.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    temp = node1
    while temp is not None:
        print(temp.val)
        temp = temp.next
    print("After:")
    x = 3
    temp = partition(node1, x)
    while temp is not None:
        print(temp.val)
        temp = temp.next
