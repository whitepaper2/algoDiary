#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 下午5:05
# @Author  : pengyuan.li
# @Site    : 
# @File    : 024_swap_pairs.py
# @Software: PyCharm

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_pairs(head):
    """
    note: 遍历该链表元素
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    pre = dummy
    pre.next = head
    while pre.next and pre.next.next:
        t = pre.next.next
        pre.next.next = t.next
        t.next = pre.next
        pre.next = t
        pre = t.next
    return dummy.next


def swap_pairs2(head):
    """
    note: 递归法,原始链表：1->2->3->4->5->6, 可以看做两部分：1）交换1->2 和 2）子结构3->4->5->6
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    temp = head.next
    head.next = swap_pairs2(head.next.next)
    temp.next = head
    return temp


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
    print("before swap:")
    while temp is not None:
        print(temp.val)
        temp = temp.next
    print("after swap:")
    temp = swap_pairs2(node1)
    while temp is not None:
        print(temp.val)
        temp = temp.next
