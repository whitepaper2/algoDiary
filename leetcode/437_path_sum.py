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


class Solution:
    def path_sum(self, root: TreeNode, sum: int) -> int:
        """
        note: 找出树中所有节点和=sum的路径个数
        :param root:
        :param sum:
        :return:
        """
        self.res = 0  # 全局变量，类，才能传递
        self.out = []

        def sub_path_sum(root, sum, cur_sum, out, res):
            if root is None or root.val is None:
                return
            cur_sum = cur_sum + root.val
            out.append(root)
            if cur_sum == sum:
                self.res += 1
            t = cur_sum
            for i in range(len(out)):
                t = t - out[i].val
                if t == sum:
                    self.res += 1
            sub_path_sum(root.left, sum, cur_sum, out, res)
            sub_path_sum(root.right, sum, cur_sum, out, res)
            out.pop()
            return self.res

        sub_path_sum(root, sum, 0, self.out, self.res)

        return self.res

    def path_sum2(self, root: TreeNode, sum: int) -> int:
        """
        note: 找出树中所有节点和=sum的路径个数,dfs
        :param root:
        :return:
        """
        import collections
        if root is None or root.val is None:
            return 0
        self.count = 0

        def dfs(cur, node):
            cur += node.val
            if cur - sum in h:
                self.count += h[cur - sum]
            if cur == sum:
                self.count += 1
            h[cur] += 1
            if node.left:
                dfs(cur, node.left)
            if node.right:
                dfs(cur, node.right)
            h[cur] -= 1
            if cur in h and h[cur] == 0:
                h.pop(cur)

        h = collections.defaultdict(int)
        dfs(0, root)
        return self.count

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
    nums = [10, 5, -3]
    sum = 15
    root = create_tree(nums)
    s = Solution()
    res = s.path_sum(root, sum)
    print(res)

    nums = [10, 5, -3]
    sum = 15
    root = create_tree(nums)
    s = Solution()
    res = s.path_sum2(root, sum)
    print(res)
