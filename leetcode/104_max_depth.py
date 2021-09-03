#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 下午8:16
# @Author  : pengyuan.li
# @Site    : 
# @File    : 104_max_depth.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(root):
    """
    note：树结构适合递归计算，root节点，左、右子树
    :type root: TreeNode
    :rtype: int
    """

    def max_depth_subtree(p):
        if p is None:
            return 0
        return 1 + max(max_depth_subtree(p.left), max_depth_subtree(p.right))

    return max_depth_subtree(root)


def max_depth2(root):
    """
    note：非递归方法，维护一个先进先出的队列，存储每一层的节点
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    else:
        out = 0
        queue = []
        queue.append(root)
        while len(queue) > 0:
            out = out + 1
            len_queue = len(queue)
            for i in range(len_queue):
                p = queue.pop()
                if p.left is not None:
                    queue.insert(0, p.left)
                if p.right is not None:
                    queue.insert(0, p.right)
        return out


if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    # right = TreeNode(2)
    root.left = left
    # root.right = right
    #
    # left2 = TreeNode(3)
    # right2 = TreeNode(4)
    # left.left = left2
    # left.right = right2

    # left3 = TreeNode(4)
    # right3 = TreeNode(3)
    # right.left = left3
    # right.right = right3

    print(max_depth2(root))
