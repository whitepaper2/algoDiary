#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 下午7:46
# @Author  : pengyuan.li
# @Site    : 
# @File    : 061_rotate_right.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def rotate_right(head, k):
    """
    note: k值可以大于链表长度，首先得到链表长度n，截断位置k%n，同时记录截断处前后连接点
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    temp = head
    before_head = head
    before_tail = None
    cnt = 0
    while temp is not None:
        cnt = cnt + 1
        before_tail = temp
        temp = temp.next
    if cnt <= 1:
        return head
    else:
        cur_cnt = k % cnt
        if cur_cnt == 0:
            return head
        else:
            temp = head
            after_cnt = 0
            after_head = None
            after_tail = None
            while temp is not None and after_cnt < cnt - cur_cnt:
                after_cnt = after_cnt + 1
                after_head = temp
                temp = temp.next
                after_tail = temp
            before_tail.next = before_head
            after_head.next = None
            return after_tail


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    # node3.next = node4
    # node4.next = node5
    temp = node1
    # print(type(temp))
    while temp is not None:
        print(temp.val)
        temp = temp.next
    print("after")
    temp = rotate_right(node1, 4)
    while temp is not None:
        print(temp.val)
        temp = temp.next
