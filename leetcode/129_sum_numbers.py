#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 下午10:10
# @Author  : pengyuan.li
# @Site    : 
# @File    : 129_sum_numbers.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sum_numbers(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def sum_numbers_dfs(root, sum_out):
        if root is None:
            return 0
        sum_out = 10 * sum_out + root.val
        if root.left is None and root.right is None:
            return sum_out
        return sum_numbers_dfs(root.left, sum_out) + sum_numbers_dfs(root.right, sum_out)

    return sum_numbers_dfs(root, 0)


if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    print(sum_numbers(root))

    root = TreeNode(4)
    left2 = TreeNode(9)
    right2 = TreeNode(0)
    root.left = left2
    root.right = right2

    left3 = TreeNode(5)
    right3 = TreeNode(1)
    left2.left = left3
    left2.right = right3
    print(sum_numbers(root))
