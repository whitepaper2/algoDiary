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
    note: 在二叉搜索树中寻找节点p和q的最小公共父节点
    递归法。1、当前节点>max(p,q),查找当前节点的左节点；2、min(p,q)<当前节点<max(p,q),返回当前节点；3、当前节点<min(p,q),查找当前节点的右节点
    :param root:
    :param p:
    :param q:
    :return:
    """
    if root is None or root.val is None:
        return None
    p_val = p.val
    q_val = q.val
    max_p_q = max(p_val, q_val)
    min_p_q = min(p_val, q_val)
    if root.val > max_p_q:
        return lowest_common_ancestor(root.left, p, q)
    elif root.val < min_p_q:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root


def lowest_common_ancestor2(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    note: 在二叉搜索树中寻找节点p和q的最小公共父节点
    循环查找。1、当前节点>max(p,q),查找当前节点的左节点；2、min(p,q)<当前节点<max(p,q),返回当前节点；3、当前节点<min(p,q),查找当前节点的右节点
    :param root:
    :param p:
    :param q:
    :return:
    """
    if root is None or root.val is None:
        return None
    p_val = p.val
    q_val = q.val
    max_p_q = max(p_val, q_val)
    min_p_q = min(p_val, q_val)
    while True:
        if root.val > max_p_q:
            root = root.left
        elif root.val < min_p_q:
            root = root.right
        else:
            break
    return root


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
    nums = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = create_tree(nums)
    p = TreeNode(2)
    q = TreeNode(8)
    res = lowest_common_ancestor2(root, p, q)
    print(res.val)

    p = TreeNode(2)
    q = TreeNode(4)
    res = lowest_common_ancestor(root, p, q)
    print(res.val)
