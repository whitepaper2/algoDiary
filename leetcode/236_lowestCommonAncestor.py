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


def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    note: 在二叉树中寻找节点p和q的最小公共父节点
    递归法。
    :param root:
    :param p:
    :param q:
    :return:
    """
    if root is None or root.val == p.val or root.val == q.val:
        return root
    left_node = lowest_common_ancestor(root.left, p, q)
    right_node = lowest_common_ancestor(root.right, p, q)
    if left_node and right_node:
        return root
    else:
        return left_node if left_node else right_node


def lowest_common_ancestor2(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    note: 在二叉树中寻找节点p和q的最小公共父节点，优化左子树，找到直接返回。
    :param root:
    :param p:
    :param q:
    :return:
    """
    if root is None or root.val == p.val or root.val == q.val:
        return root
    left_node = lowest_common_ancestor(root.left, p, q)
    if left_node and left_node != p and left_node != q:
        return left_node
    right_node = lowest_common_ancestor(root.right, p, q)
    if left_node and right_node:
        return root
    else:
        return left_node if left_node else right_node


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
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_tree(nums)
    p = TreeNode(5)
    q = TreeNode(1)
    res = lowest_common_ancestor(root, p, q)
    print(res.val)

    p = TreeNode(5)
    q = TreeNode(4)
    res = lowest_common_ancestor2(root, p, q)
    print(res.val)
