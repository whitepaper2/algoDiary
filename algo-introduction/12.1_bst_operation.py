#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 下午4:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 12.1_bst_operation.py
# @Software: PyCharm


class TNode:
    def __init__(self, x):
        self.val = x
        self.leftNode = None
        self.rightNode = None


class BST:
    def __init__(self, x):
        self.root = TNode(x)

    # def __init__(self, nums):
    #     self.root = TNode(nums[0])
    #     for x in nums[1:]:
    #         self.insert(root, x)

    # 基本操作：增、删、改、查
    def insert(self, root, x):
        if not root or not root.val:
            root = TNode(x)
        elif root.val > x:
            root.leftNode = self.insert(root.leftNode, x)
        elif root.val < x:
            root.rightNode = self.insert(root.rightNode, x)

        return root

    def create(self, nums):
        for num in nums:
            self.insert(self.root, num)

    def _inorder(self, out, root):
        if not root:
            return
        self._inorder(out, root.leftNode)
        out.append(root.val)
        self._inorder(out, root.rightNode)

    def inorder(self, root):
        out = []
        self._inorder(out, root)
        return out

    def inorderWalk(self, root):
        if not root:
            return
        self.inorderWalk(root.leftNode)
        print(root.val)
        self.inorderWalk(root.rightNode)

    def query(self, root, x):
        if not root:
            return False
        if root.val == x:
            return True
        elif root.val > x:
            return self.query(root.leftNode, x)
        else:
            return self.query(root.rightNode, x)

    def getMin(self, root):
        if root.leftNode:
            return self.getMin(root.leftNode)
        else:
            return root

    def delete(self, root, x):
        if not root:
            return
        if root.val > x:
            root.leftNode = self.delete(root.leftNode, x)
        elif root.val < x:
            root.rightNode = self.delete(root.rightNode, x)
        else:
            if root.leftNode and root.rightNode:
                tmp = self.getMin(root.rightNode)
                root.val = tmp.val
                root.rightNode = self.delete(root.rightNode, tmp.val)
                pass
            elif root.leftNode and not root.rightNode:
                root = root.leftNode
            elif not root.leftNode and root.rightNode:
                root = root.rightNode
            else:
                root = None
        return root


if __name__ == "__main__":
    nums = [1, 4, 5, 10, 16, 17, 21]
    # root = TNode(13)
    bst = BST(13)
    root = bst.root
    bst.create(nums)
    # for num in nums:
    #     root = bst.insert(root, num)
    out = bst.inorder(root)
    print(out)
    print(bst.getMin(root))
    bst.delete(root, 17)
    print('after delete:')
    bst.inorderWalk(root)
    print('*****', root.val)
    print(bst.getMin(root).val)
    print(bst.query(root, 13))
    # dummy.insert()
