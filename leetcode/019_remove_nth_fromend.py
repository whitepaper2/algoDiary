#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 下午5:37
# @Author  : pengyuan.li
# @Site    : 
# @File    : 019_remove_nth_fromend.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_fromend(head, n):
    """
    note: 一次遍历删除法。记录两个指针pre/cur，cur遍历到nth，pre再开始遍历。
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if head is None:
        return []
    pre = head
    cur = head
    for i in range(n):
        cur = cur.next
    if cur is None:
        return head.next
    while cur.next is not None:
        pre = pre.next
        cur = cur.next
    pre.next = pre.next.next
    return head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    temp = node1
    # print(type(temp))
    while temp is not None:
        print(temp.val)
        temp = temp.next
    print("after")
    temp = remove_nth_fromend(node1, 5)
    while temp is not None:
        print(temp.val)
        temp = temp.next
