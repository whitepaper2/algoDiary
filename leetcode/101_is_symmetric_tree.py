#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 下午12:55
# @Author  : pengyuan.li
# @Site    : 
# @File    : 101_is_symmetric_tree.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_symmetric(root):
    """
    note: 寻找对称树，要维护left\right两个指针，迭代比较是否相等
    :type root: TreeNode
    :rtype: bool
    """

    def is_symmetric_subtree(p0, q0):

        if p0 is None and q0 is None:
            return True
        elif p0 is None or q0 is None:
            return False
        else:
            if p0.val != q0.val:
                return False
            else:
                is_left = is_symmetric_subtree(p0.left, q0.right)
                is_right = is_symmetric_subtree(p0.right, q0.left)
            return is_left and is_right

    if root is None:
        return True
    return is_symmetric_subtree(root.left, root.right)


def is_symmetric2(root):
    """
    note: 寻找对称树，要维护left\right两个指针，遇到空值断开这次循环，效率较高
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    q1 = []
    q2 = []
    q1.append(root.left)
    q2.append(root.right)
    while len(q1) > 0 and len(q2) > 0:
        left = q1.pop()
        right = q2.pop()
        if right is None or left is None:
            if right is None and left is None:
                continue
            else:
                return False
        else:
            if left.val != right.val:
                return False
            else:
                q1.insert(0, left.left)
                q2.insert(0, right.right)
                q1.insert(0, left.right)
                q2.insert(0, right.left)
    return True


if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(2)
    root.left = left
    root.right = right

    left2 = TreeNode(3)
    right2 = TreeNode(4)
    left.left = left2
    left.right = right2

    left3 = TreeNode(4)
    right3 = TreeNode(3)
    right.left = left3
    right.right = right3

    print(is_symmetric2(root))
    # print(is_same_tree(root, root2))
