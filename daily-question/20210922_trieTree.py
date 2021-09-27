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


"""
前缀统计：统计有多少个字符串是T的前缀
words = ["w", "wo", "wor", "worl", "world", "worw", "wo"]
prefix = "world"
"""


def getPrefixCnts(words, prefix):
    """
    遍历法，1.求出所有前缀集合，2.前缀出现的次数求和
    :param words:
    :param prefix:
    :return:
    """
    preWords = list()
    for i, s in enumerate(prefix):
        if i == 0:
            preWords.append(prefix[0])
        else:
            preWords.append(preWords[-1] + s)
    from collections import Counter
    wordDict = Counter(words)
    res = 0
    for s in preWords:
        res += wordDict[s]
    return res


def getPrefixCnts2(words, prefix):
    """
    构造前缀字典树
    :param words:
    :param prefix:
    :return:
    """

    class TrieCntNode(object):
        def __init__(self):
            self.children = defaultdict(TrieCntNode)
            self.isEnd = False
            self.cnts = 0

    class TrieCntTree(object):
        def __init__(self):
            self.root = TrieCntNode()

        def insert(self, word):
            cur = self.root
            for w in word:
                cur = cur.children[w]
            cur.cnts += 1
            cur.isEnd = True

        def getCnts(self, word):
            res = 0
            cur = self.root
            for w in word:
                child = cur.children.get(w)
                if child is not None:
                    res += child.cnts
                cur = child
            return res

    tree = TrieCntTree()
    for w in words:
        tree.insert(w)

    return tree.getCnts(prefix)


if __name__ == "__main__":
    # words = ["w", "wo", "wor", "worl", "world"]
    # print(getMaxWord(words))

    words = ["w", "wo", "wor", "worl", "world", "worw", "wo"]
    prefix = "world"
    print(getPrefixCnts(words, prefix))

    words = ["w", "wo", "wor", "worl", "world", "worw", "wo"]
    prefix = "world"
    print(getPrefixCnts2(words, prefix))
