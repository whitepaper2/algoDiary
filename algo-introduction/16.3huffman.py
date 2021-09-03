#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 下午3:25
# @Author  : pengyuan.li
# @Site    : 
# @File    : 16.3huffman.py
# @Software: PyCharm
import heapq


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class HuffmanTree:
    def __init__(self):
        pass


def createHuffmanTree(strsDict):
    """
    note:构造huffman树，返回根节点
    :param strsDict:
    :return:
    """
    queue = [(v, TreeNode((v, k))) for k, v in strsDict.items()]
    heapq.heapify(queue)
    while len(queue) > 1:
        n1, t1 = heapq.heappop(queue)
        n2, t2 = heapq.heappop(queue)
        z = TreeNode((n1 + n2, None))
        z.left = t1
        z.right = t2
        heapq.heappush(queue, (n1 + n2, z))
    return queue[-1]


def inorderTravel(root):
    if not root:
        return
    inorderTravel(root.left)
    print(root.val)
    inorderTravel(root.right)


encodeDict = dict()
decodeDict = dict()


def genHuffmanDict(root, cur):
    """
    note:生成编码和解码字典
    :param root:
    :param cur:
    :return:
    """
    if not root:
        return
    genHuffmanDict(root.left, cur + '0')
    v, k = root.val
    if k:
        encodeDict[k] = cur
        decodeDict[cur] = k
    genHuffmanDict(root.right, cur + '1')


def huffmanEncode(strs):
    if len(strs) == 0:
        return strs
    out = ""
    for s in strs:
        out += encodeDict[s]

    return out


def huffmanDecode(strs):
    if len(strs) == 0:
        return strs
    out = ""
    tmp = ""
    for s in strs:
        tmp += s
        if decodeDict.get(tmp):
            out += decodeDict[tmp]
            tmp = ""
    return out


if __name__ == "__main__":
    strsDict = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}
    root = createHuffmanTree(strsDict)
    inorderTravel(root[1])
    genHuffmanDict(root[1], '')
    print(encodeDict, decodeDict)
    print(huffmanEncode("abcd"))
    print(huffmanDecode("0101100111"))
