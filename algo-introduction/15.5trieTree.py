#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 下午5:38
# @Author  : pengyuan.li
# @Site    : 
# @File    : 15.5trieTree.py
# @Software: PyCharm
import networkx

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
