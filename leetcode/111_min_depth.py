#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 下午12:17
# @Author  : pengyuan.li
# @Site    : 
# @File    : 111_min_depth.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def min_depth3(root):
    """
    note：非递归方法，维护一个先进先出的队列，存储每一层的节点，遇到左右子节点都是空值，则直接返回该值即是树的最小深度
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    out = 0
    queue = []
    queue.append(root)
    while len(queue) > 0:
        out = out + 1
        len_queue = len(queue)
        for i in range(len_queue):
            p = queue.pop()
            if p.left is None and p.right is None:
                return out
            if p.left is not None:
                queue.insert(0, p.left)
            if p.right is not None:
                queue.insert(0, p.right)


def min_depth(root):
    """
    note：树结构适合递归计算，root节点，左、右子树
    :type root: TreeNode
    :rtype: int
    """

    def min_depth_subtree(p):
        if p is None:
            return 0
        if p.left is None:
            return 1 + min_depth_subtree(p.right)
        if p.right is None:
            return 1 + min_depth_subtree(p.left)
        return 1 + min(min_depth_subtree(p.left), min_depth_subtree(p.right))

    return min_depth_subtree(root)


def min_depth2(root):
    """
    note：树结构适合递归计算，root节点，左、右子树，该方法运行时间长，每次都计算左右子树
    :type root: TreeNode
    :rtype: int
    """

    def min_depth_subtree(p):
        if p is None:
            return 0
        left_min_depth = min_depth_subtree(p.left)
        right_min_depth = min_depth_subtree(p.right)
        if left_min_depth == 0 or right_min_depth == 0:
            return 1 + max(left_min_depth, right_min_depth)
        return 1 + min(left_min_depth, right_min_depth)

    return min_depth_subtree(root)


if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    # right = TreeNode(2)
    root.left = left
    # root.right = right
    #
    left2 = TreeNode(3)
    right2 = TreeNode(4)
    left.left = left2
    left.right = right2

    # left3 = TreeNode(4)
    # right3 = TreeNode(3)
    # right.left = left3
    # right.right = right3

    print(min_depth2(root))
    print(min_depth(root))
    print(min_depth3(root))
