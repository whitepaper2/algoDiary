#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 上午11:17
# @Author  : pengyuan.li
# @Site    : 
# @File    : 110_is_balanced.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_balanced(root):
    """
    note:迭代法，树是否平衡，观察左右子树是否平衡且左右树高度大于1时，高度差是否大于1
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True

    def subtree_balanced_depth(p):
        if p is None:
            return True, 0
        left_is_balanced, left_depth = subtree_balanced_depth(p.left)
        right_is_balanced, right_depth = subtree_balanced_depth(p.right)
        if left_is_balanced and right_is_balanced:
            if (left_depth > 1 or right_depth > 1) and abs(left_depth - right_depth) > 1:
                return False, -1
            else:
                return True, max(left_depth, right_depth) + 1
        else:
            return False, -1

    flag, depth = subtree_balanced_depth(root)
    return flag, depth


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

    print(is_balanced(root))
