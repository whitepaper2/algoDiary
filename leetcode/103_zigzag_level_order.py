#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 下午9:29
# @Author  : pengyuan.li
# @Site    : 
# @File    : 102_level_order.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzag_level_order(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    queue = []
    queue.append(root)
    out = []
    is_right = False
    while len(queue) > 0:
        len_queue = len(queue)
        temp_out = []
        for i in range(len_queue):
            p = queue.pop()
            temp_out.append(p.val)
            if p.left is not None:
                queue.insert(0, p.left)
            if p.right is not None:
                queue.insert(0, p.right)
        if is_right:
            temp_out = list(reversed(temp_out))
        out.append(temp_out)
        is_right = False if is_right else True
    return out


def zigzag_level_order2(root):
    """
    note: 维护两个栈结构q1,q2,以相反方法保留相邻层的元素
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    queue1 = []
    queue2 = []
    queue1.append(root)
    out = []
    while len(queue1) > 0 or len(queue2) > 0:
        temp_out = []
        for i in range(len(queue1)):
            p = queue1.pop()
            temp_out.append(p.val)
            if p.left is not None:
                queue2.append(p.left)
            if p.right is not None:
                queue2.append(p.right)
        out.append(temp_out)
        temp_out = []
        for i in range(len(queue2)):
            p = queue2.pop()
            temp_out.append(p.val)
            if p.right is not None:
                queue1.append(p.right)
            if p.left is not None:
                queue1.append(p.left)
        if len(temp_out):
            out.append(temp_out)
    return out


if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right

    left2 = TreeNode(5)
    right2 = TreeNode(6)
    left.left = left2
    left.right = right2

    left3 = TreeNode(7)
    right3 = TreeNode(8)
    right.left = left3
    right.right = right3

    print(zigzag_level_order(root))
    print(zigzag_level_order2(root))
