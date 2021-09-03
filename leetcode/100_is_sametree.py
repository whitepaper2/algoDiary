#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 下午5:32
# @Author  : pengyuan.li
# @Site    : 
# @File    : 100_is_sametree.py
# @Software: PyCharm

from common import timeit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


@timeit
def is_same_tree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """

    def is_same_subtree(p0, q0):

        if p0 is None and q0 is None:
            return True
        elif p0 is not None and q0 is not None:
            out = True if p0.val == q0.val else False
            left = is_same_subtree(p0.left, q0.left)
            right = is_same_subtree(p0.right, q0.right)
            return out and left and right
        else:
            return False

    return is_same_subtree(p, q)


@timeit
def is_same_tree2(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """

    def is_same_subtree(p0, q0):

        if p0 is None and q0 is None:
            return True
        elif p0 is not None and q0 is not None:
            out = True if p0.val == q0.val else False
            if out:
                left = is_same_subtree(p0.left, q0.left)
                right = is_same_subtree(p0.right, q0.right)
                return left and right
            else:
                return False
        else:
            return False

    return is_same_subtree(p, q)


if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    root2 = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(3)
    root2.left = left
    root2.right = right

    print(is_same_tree2(root, root2))
    # print(is_same_tree(root, root2))
