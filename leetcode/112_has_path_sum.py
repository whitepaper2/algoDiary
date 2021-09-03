#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 下午5:31
# @Author  : pengyuan.li
# @Site    : 
# @File    : 112_has_path_sum.py
# @Software: PyCharm

from common import timeit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


@timeit
def has_path_sum(root, sum):
    """
    note: 迭代法，可以看做求子树的路径和是否等于给定值，判断条件多，执行更快
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root is None and sum is None:
        return True
    if root is None or sum is None:
        return False

    def has_subtree_path(p, cur_sum):
        if p.left is None and p.right is None:
            return p.val == cur_sum
        elif p.left is not None and p.right is None:
            return has_subtree_path(p.left, cur_sum - p.val)
        elif p.left is None and p.right is not None:
            return has_subtree_path(p.right, cur_sum - p.val)
        else:
            return has_subtree_path(p.left, cur_sum - p.val) or has_subtree_path(p.right, cur_sum - p.val)

    return has_subtree_path(root, sum)


@timeit
def has_path_sum2(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root is None and sum is None:
        return True
    if root is None or sum is None:
        return False

    def has_subtree_path(p, cur_sum):
        if p.left is None and p.right is None:
            return p.val == cur_sum
        return has_subtree_path(p.left, cur_sum - p.val) or has_subtree_path(p.right, cur_sum - p.val)

    return has_subtree_path(root, sum)


if __name__ == "__main__":
    root = TreeNode(5)
    left = TreeNode(4)
    right = TreeNode(8)
    root.left = left
    root.right = right

    left2 = TreeNode(11)
    left.left = left2

    left3 = TreeNode(13)
    right3 = TreeNode(4)
    right.left = left3
    right.right = right3

    left4 = TreeNode(7)
    right4 = TreeNode(2)
    left2.left = left4
    left2.right = right4

    right5 = TreeNode(1)
    right3.right = right5
    print(has_path_sum(root, 22))
    print(has_path_sum2(root, 22))
