#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 下午6:22
# @Author  : pengyuan.li
# @Site    : 
# @File    : 235_lowestCommonAncestor.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sum_left_leaves(root: TreeNode) -> int:
    """
    note: 在二叉树中计算所有左叶子之和
    递归法。
    :param root:
    :return:
    """
    if root is None or root.val is None:
        return 0

    if root.left and root.left.val is not None and (root.left.left is None or root.left.left.val is None) and (
            root.left.right is None or root.left.right.val is None):
        return root.left.val + sum_left_leaves(root.right)
    return sum_left_leaves(root.left) + sum_left_leaves(root.right)


def sum_left_leaves2(root: TreeNode) -> int:
    """
    note: 在二叉树中计算所有左叶子节点之和。
    首先判断是否左节点，再判断是否叶子节点
    :param root:
    :return:
    """
    if root is None or root.val is None:
        return 0
    left_sum = 0
    queue = [(root, False)]  # 是否左节点
    while len(queue) > 0:
        cur = queue.pop(0)
        node = cur[0]
        status = cur[1]
        if node is not None and node.val is not None:
            flag = True  # 是否叶子节点
            if node.left is not None and node.left.val is not None:
                queue.append((node.left, True))
                flag = False
            if node.right is not None and node.right.val is not None:
                queue.append((node.right, False))
                flag = False
            if status and flag:
                left_sum = left_sum + node.val

    return left_sum


def create_tree(nums):
    node_list = []
    for ele in nums:
        node = TreeNode(ele)
        node_list.append(node)
    for i in range(len(node_list) // 2):
        node_list[i].left = node_list[2 * i + 1]
        node_list[i].right = node_list[2 * i + 2]
    return node_list[0]


if __name__ == "__main__":
    nums = [3, 9, 20, None, None, 15, 7]
    root = create_tree(nums)
    res = sum_left_leaves2(root)
    print(res)

    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_tree(nums)
    res = sum_left_leaves2(root)
    print(res)
