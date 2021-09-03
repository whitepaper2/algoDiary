#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 下午3:03
# @Author  : pengyuan.li
# @Site    : 
# @File    : 141_has_cycle.py
# @Software: PyCharm


# note:线性单链表是否有环，要求无重复元素
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
    """
    note：使用具有无重复集合or字典，线性判断元素是否已存在
    :type head: ListNode
    :rtype: bool
    """
    user_dict = {}
    if head is None or head.next is None:
        return False
    while head:
        if user_dict.get(head) is not None:
            return True
        else:
            user_dict[head] = 1
        head = head.next
    return False


def has_cycle2(head):
    """
    note：使用具有无重复集合or字典，线性判断元素是否已存在
    :type head: ListNode
    :rtype: bool
    """
    user_set = set()
    if head is None or head.next is None:
        return False
    while head:
        if head in user_set:
            return True
        else:
            user_set.add(head)
        head = head.next
    return False


def has_cycle3(head):
    """
    note：维护快、慢双指针。如果链表中存在环，快指针可以追上慢指针
    :type head: ListNode
    :rtype: bool
    """
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    temp = node1
    print(has_cycle3(temp))

    node1 = ListNode(3)
    node2 = ListNode(3)
    node3 = ListNode(3)
    # node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    # node3.next = node4
    # node4.next = node2

    temp = node1
    print(has_cycle3(temp))
