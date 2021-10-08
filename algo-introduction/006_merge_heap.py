#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 下午9:13
# @Author  : pengyuan.li
# @Site    : 
# @File    : 006_merge_heap.py
# @Software: PyCharm
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(nums):
    node_list = []
    for ele in nums:
        node = TreeNode(ele)
        node_list.append(node)
    for i in range(len(node_list) // 2):
        node_list[i].left = node_list[2 * i + 1]
        node_list[i].right = node_list[2 * i + 2]
    return node_list[0]


def adjust_maxheap(nums: List[int], i: int, n: int):
    """
    调整最大堆的结构
    :param nums: 原始数组
    :param i: 第i个节点
    :param n: 数组大小
    :return:
    """
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and nums[left] > nums[i]:
        largest = left
    else:
        largest = i
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        tmp = nums[largest]
        nums[largest] = nums[i]
        nums[i] = tmp
        adjust_maxheap(nums, largest, n)


def build_maxheap(nums: List[int], n: int):
    """
    自下而上建立最大堆
    :param nums: 原始数组
    :param n: 原始数组大小
    :return:
    """
    for i in range(n // 2, -1, -1):
        adjust_maxheap(nums, i, n)


def merge_heap(nums1: TreeNode, nums2: TreeNode):
    """
    note:合并两个大小相同的堆，最小堆+最小堆，最小堆+最大堆，最大堆+最大堆
    :param nums1:
    :param nums2:
    :return: 最大堆
    """
    out = []
    queue = [nums1, nums2]
    while len(queue) > 0:
        ele = queue.pop(0)
        out.append(ele.val)
        if ele.left:
            queue.append(ele.left)
        if ele.right:
            queue.append(ele.right)
    print(out)
    new_out = out[:-1]
    new_out.insert(0, out[-1])
    build_maxheap(new_out, len(out))
    return new_out


if __name__ == "__main__":
    nums1 = [9, 4, 7, 2, 1, 6, 5]
    root1 = create_tree(nums1)
    nums2 = [20, 18, 16, 14, 12, 10, 9]
    root2 = create_tree(nums2)
    out = merge_heap(root1, root2)
    print(out)
