#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 下午2:43
# @Author  : pengyuan.li
# @Site    : 
# @File    : 108_sorted_array_bst.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sorted_array_bst(nums):
    """
    note：怎么保证这种算法左右子树高度差不超过1 ？
    :type nums: List[int]
    :rtype: TreeNode
    """
    len_nums = len(nums)

    def sorted_subarray_bst(nums, left, right):
        if left > right:
            return None
        middle = int((left + right) / 2)
        cur_root = TreeNode(nums[middle])
        cur_root.left = sorted_subarray_bst(nums, left, middle - 1)
        cur_root.right = sorted_subarray_bst(nums, middle + 1, right)
        return cur_root

    return sorted_subarray_bst(nums, 0, len_nums - 1)


if __name__ == "__main__":
    """
    note:所谓二叉搜索树，是一种始终满足左<根<右的特性，如果将二叉搜索树按中序遍历的话，得到的就是一个有序数组了。
    一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
    """
    nums = [-10, -3, 0, 5, 9]
    root = sorted_array_bst(nums)

    # 中序遍历算法
    def print_by_order(p):
        if p is not None:
            print_by_order(p.left)
            print(p.val)
            print_by_order(p.right)


    print_by_order(root)
