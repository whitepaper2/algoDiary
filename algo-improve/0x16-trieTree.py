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

from collections import defaultdict, Counter
from typing import List


class TrieNode(object):

    def __init__(self):
        self.isEnd = False
        self.children = defaultdict(TrieNode)


class Trie(object):

    def __init__(self, N=32):
        self.root = TrieNode()
        self.N = N

    def insert(self, word):
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.isEnd = True

    def search(self, word):
        cur = self.root
        for s in word:
            cur = cur.children.get(s)
            if cur is None:
                return False
        return cur.isEnd == True

    def getXor(self, word):
        res = 0
        cur = self.root
        for i, s in enumerate(word):
            s2 = str(int(s) ^ 1)
            if cur.children:
                if s2 in cur.children:
                    res += 1 << (self.N - i - 1)
                    cur = cur.children.get(s2)
                else:
                    cur = cur.children.get(s)
        return res


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

    wordDict = Counter(words)
    res = 0
    for s in preWords:
        res += wordDict[s]
    return res


def getPrefixCnts2(words, prefix):
    """
    构造前缀字典树，叶子节点的数量相加
    :param words:
    :param prefix:
    :return:
    """

    class TrieCntNode(object):

        def __init__(self):
            self.children = defaultdict(TrieCntNode)
            self.cnts = 0

    class TrieCntTree(object):

        def __init__(self):
            self.root = TrieCntNode()

        def insert(self, word):
            cur = self.root
            for w in word:
                cur = cur.children[w]
            # 叶子节点+1
            cur.cnts += 1

        def getCnts(self, word):
            res = 0
            cur = self.root
            for w in word:
                child = cur.children.get(w)
                if child is None:
                    break
                res += child.cnts
                cur = child
            return res

    tree = TrieCntTree()
    for w in words:
        tree.insert(w)

    return tree.getCnts(prefix)


def maxXorPairs(A: List[int]) -> int:
    """
    note:在一系列整数中，寻找最大的异或对，max(A[i] xor A[j]), 0<=i<n,i<j
    整数表示为32位二进制数，构造字典树，贪心寻找，每次与当前值相反的数
    Arguments
    ---------
    A:List[int]
    Returns
    -------
    int
    """
    # 暴力解法
    # nums = [2,4,5,6,7]
    # max(i^j for i in range(len(nums)) for j in range(i+1,len(nums)))
    N = 32
    B = []
    res = 0
    for a in A:
        a2 = bin(a)[2:]
        B.append("".join([str(0)] * (N - len(a2))) + a2)
    trie = Trie(N)
    for b in B:
        res = max(res, trie.getXor(b))
        trie.insert(b)
    return res


def xorLongestPath():
    """
    note:树上边，x和y权值最大异或值
    D[x]：root到x路径上所有边权的异或值，= D[father(x)] xor weight(father(x),x)
    """
    outEdges = [[1, 2, 3], [1, 3, 4], [1, 4, 3], [2, 5, 10], [2, 6, 8],
                [4, 7, 2], [4, 8, 5], [7, 9, 1]]
    adj = defaultdict(list)
    vertices = set()
    for u, v, w in outEdges:
        adj[u].append((v, w))
        vertices.add(u)
        vertices.add(v)
    # root = 1
    n = len(vertices)
    dist = [0] * (n + 1)

    def dfs(root):
        if root in adj:
            for v, w in adj[root]:
                dist[v] = w ^ dist[root]
                dfs(v)

    dfs(1)
    # print(dist)
    return maxXorPairs(dist)


# @todo:两个字典树合并问题

if __name__ == "__main__":
    words = ["w", "wo", "wor", "worl", "world"]
    print(getMaxWord(words))

    words = ["w", "wo", "wor", "worl", "world", "worw", "wo"]
    prefix = "world"
    print(getPrefixCnts(words, prefix))

    words = ["wo", "wor", "worl", "world", "worw", "wo"]
    prefix = "world"
    print(getPrefixCnts2(words, prefix))

    words = ['ant', 'act', 'ackt']
    trie = Trie()
    for word in words:
        trie.insert(word)
    print(trie.search('act'))

    print(maxXorPairs([2, 4, 5, 6, 7]))

    print(xorLongestPath())