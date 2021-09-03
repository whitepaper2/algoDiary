#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 下午4:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 12.1_bst_operation.py
# @Software: PyCharm


class TNode(object):
    def __init__(self, x):
        self.val = x
        self.leftNode = None
        self.rightNode = None
        self.color = "BLACK"
        self.parent = None


class RBTree(object):
    def __init__(self):
        self.nil = TNode(0)
        self.root = self.nil

    def LeftRotate(self, T, x):
        y = x.rightNode
        x.rightNode = y.leftNode
        if y.leftNode != T.nil:
            y.leftNode.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.leftNode:
            x.parent.leftNode = y
        else:
            x.parent.rightNode = y
        y.leftNode = x
        x.parent = y

    def RightRotate(self, T, x):
        y = x.leftNode
        x.leftNode = y.rightNode
        if y.rightNode != T.nil:
            y.rightNode.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.rightNode:
            x.parent.rightNode = y
        else:
            x.parent.leftNode = y
        y.rightNode = x
        x.parent = y

    # 基本操作：增、删、改、查
    def RBInsertFix(self, T, x):
        while x.parent.color == "RED":
            if x.parent == x.parent.parent.leftNode:
                y = x.parent.parent.rightNode
                if y.color == "RED":
                    x.parent.color = "BLACK"
                    y.color = "BLACK"
                    x.parent.parent.color = "RED"
                    x = x.parent.parent
                elif x == x.parent.rightNode:
                    x = x.parent
                    self.LeftRotate(T, x)
                x.parent.color = "BLACK"
                x.parent.parent.color = "RED"
                self.RightRotate(T, x.parent.parent)
            else:
                y = x.parent.parent.leftNode
                if y.color == "RED":
                    x.parent.color = "BLACK"
                    y.color = "BLACK"
                    x.parent.parent.color = "RED"
                    x = x.parent.parent
                else:
                    if x == x.parent.leftNode:
                        x = x.parent
                        self.RightRotate(T, x)
                    x.parent.color = "BLACK"
                    x.parent.parent.color = "RED"
                    self.LeftRotate(T, x.parent.parent)

        T.root.color = "BLACK"

    def RBinsert(self, T, z):
        """
        :param T: red-black tree
        :param z: TNode
        :return:
        """
        x = T.root
        y = T.nil
        while x != T.nil:
            y = x
            if z.val < x.val:
                x = x.leftNode
            else:
                x = x.rightNode
        z.parent = y
        if y == T.nil:
            T.root = z
        elif y.val > z.val:
            y.leftNode = z
        else:
            y.rightNode = z
        z.color = "RED"
        z.leftNode = T.nil
        z.rightNode = T.nil
        self.RBInsertFix(T, z)
        return "insert {}".format(z.val)

    def create(self, T, nums):
        for num in nums:
            self.RBinsert(T, TNode(num))

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
        if root != None:
            self.inorderWalk(root.leftNode)
            if root.val != 0:
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

    def transplant(self, T, u, v):
        """
        以v为根节点的子树代替以u为根节点的子树
        :param T:
        :param u:
        :param v:
        :return:
        """
        if u == self.nil:
            T.root = v
        elif u == u.parent.leftNode:
            u.parent.leftNode = v
        else:
            u.parent.rightNode = v
        if v != self.nil:
            v.parent = u.parent

    def delete(self, T, z):
        """
        删除节点z
        :param T:
        :param z:
        :return:
        """
        if z.leftNode == self.nil:
            self.transplant(T, z, z.rightNode)
        elif z.rightNode == self.nil:
            self.transplant(T, z, z.leftNode)
        else:

            pass
        pass


if __name__ == "__main__":
    nums = [1, 4, 5, 10, 16, 17, 21]
    T = RBTree()

    for num in nums:
        print(T.RBinsert(T, TNode(num)))
    print("root=", T.root.val)
    T.inorderWalk(T.root)
