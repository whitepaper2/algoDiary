#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 下午8:14
# @Author  : pengyuan.li
# @Site    : 
# @File    : 113_path_sum.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def path_sum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    out = []
    cur = []
    from copy import deepcopy

    def path_sum_dfs(root, sum, cur, out):
        if root is None:
            return
        cur.append(root.val)
        if root.val == sum and root.left is None and root.right is None:
            out.append(deepcopy(cur))
        path_sum_dfs(root.left, sum - root.val, cur, out)
        path_sum_dfs(root.right, sum - root.val, cur, out)
        cur.pop()

    path_sum_dfs(root, sum, cur, out)
    return out


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

    left5 = TreeNode(5)
    right5 = TreeNode(1)
    right3.right = right5
    right3.left = left5
    print(path_sum(root, 22))
