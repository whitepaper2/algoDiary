#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 下午3:25
# @Author  : pengyuan.li
# @Site    : 
# @File    : 16.3huffman.py
# @Software: PyCharm

_M = 5


class BKeyword(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data


class BNode(object):
    def __init__(self):
        self._parent = None
        self.keywords = []
        self.child_nodes = []

    def set_parent(self, node):
        self._parent = node
        if node.get_parent() is None:
            global root_node
            root_node = node.get_parent()

    def get_parent(self):
        return self._parent

    def insert_child_node(self, index, add_node):
        add_node.set_parent(self)
        self.child_nodes.insert(index, add_node)

    def append_child_node(self, add_node):
        add_node.set_parent(self)
        self.child_nodes.append(add_node)

    def find_add_index(self, add_word):
        if len(self.keywords) == 0:
            return 0
        index = 0
        while True:
            if index >= len(self.keywords):
                break
            key = self.keywords[index].key
            if add_word.key < key:
                break
            index += 1
        return index

    def blind_add(self, word: BKeyword):
        index = self.find_add_index(word)
        self.keywords.insert(index, word)

    def split(self):
        parent, center_keyword, left_node, right_node = self.split_to_piece()
        parent_add_index = parent.find_add_index(center_keyword)
        parent.insert_child_node(parent_add_index, right_node)
        parent.insert_child_node(parent_add_index, left_node)
        if self in parent.child_nodes:
            parent.child_nodes.remove(self)
        parent.add_word(center_keyword, force=True)
        root = self
        while root.get_parent() is not None:
            root = root.get_parent()
        global root_node
        root_node = root

    def split_to_piece(self):
        center_keyword = self.keywords[(_M - 1) // 2]
        if self.get_parent() is None:
            self.set_parent(BNode())
        left_node = BNode()
        right_node = BNode()
        for keyword in self.keywords:
            if keyword.key < center_keyword.key:
                left_node.keywords.append(keyword)
            elif keyword.key > center_keyword.key:
                right_node.keywords.append(keyword)
        for i in range(len(self.child_nodes)):
            if i <= (len(self.child_nodes) - 1) // 2:
                left_node.append_child_node(self.child_nodes[i])
            else:
                right_node.append_child_node(self.child_nodes[i])
        return self.get_parent(), center_keyword, left_node, right_node

    def add_word(self, keyword, force=False):
        if keyword.key == 0:
            print("")
        # 叶子节点 或 进位添加
        if len(self.child_nodes) == 0 or force:
            if keyword.key == 20:
                print("")
            self.blind_add(keyword)
            if len(self.keywords) == _M:
                # 开始分裂
                print("新增:" + str(keyword.key) + ", 达到m值，分裂")
                self.split()
        else:
            # 非叶子节点
            index = self.find_add_index(keyword)
            if index >= len(self.child_nodes):
                index = index - 1
            self.child_nodes[index].add_word(keyword)


import random
from random import shuffle


def prepare():
    array = []
    number = 0
    for i in range(200):
        number = number + random.randint(1, 4)
        # number = number + 1
        array.append(number)
    shuffle(array)
    return array


if __name__ == '__main__':
    root_node = BNode()
    array = prepare()
    for i in array:
        keyword = BKeyword(i, "数据" + str(i))
        root_node.add_word(keyword)
    print(root_node)
