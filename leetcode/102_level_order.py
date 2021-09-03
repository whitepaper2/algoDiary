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


def level_order(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    queue = []
    queue.append(root)
    out = []
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

    print(level_order(root))
