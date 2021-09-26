#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 下午8:59
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20210922_trieTree.py
# @Software: PyCharm

"""
前缀树，字符串由小写字母表示
"""

from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.isEnd = False
        self.children = defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.isEnd = True

    def search(self, word):
        cur = self.root
        for s in word:
            cur = cur.children.get(s)
            if cur is None or not cur.isEnd:
                return False
        return True


def getMaxWord(words):
    res = ''
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        if trie.search(word):
            if len(word) > len(res):
                res = word
            elif len(word) == len(res) and word > res:
                res = word
    return res





if __name__ == "__main__":
    words = ["w", "wo", "wor", "worl", "world"]

    print(getMaxWord(words))

