#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 下午2:01
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1_2_insertion_sort.py
# @Software: PyCharm

PARENT = lambda i: i // 2
LEFT = lambda i: 2 * i + 1
RIGHT = lambda i: 2 * i + 2


def maxHeapify(A, i, heapSize):
    """
    假设以left(i)\right(i)为根节点的子树都满足最大堆性质，判断当前节点是否满足堆性质，若满足不调整，否则向下调整
    :param A:
    :param i:
    :param heapSize:
    :return:
    """
    left, right = LEFT(i), RIGHT(i)
    if left < heapSize and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right < heapSize and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest, heapSize)


def buildMaxHeap(A):
    """
    给定无序数组构造最大堆
    :param A:
    :return:
    """
    lenA = len(A)
    for i in range(lenA // 2, -1, -1):
        maxHeapify(A, i, lenA)


def sortByMaxHeap(A):
    buildMaxHeap(A)
    heapSize = len(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapSize -= 1
        maxHeapify(A, 0, heapSize)


def extractHeapMaximum(A, heapSize):
    if heapSize < 1:
        raise Exception("heap under flow")
    maxVal = A[0]
    A[0] = A[heapSize - 1]
    maxHeapify(A, 0, heapSize - 1)
    return maxVal


def heapMaximum(A):
    return A[0]


def heapIncreaseKey(A, i, key):
    """
    位置i,更新关键字值为key
    :param A:
    :param i:
    :param key:
    :return:
    """
    if A[i] > key:
        raise Exception("key smaller than current A[i]")
    A[i] = key
    while i >= 0 and A[PARENT(i)] < A[i]:
        A[i], A[PARENT(i)] = A[PARENT(i)], A[i]
        i = PARENT(i)


def maxHeapInsert(A, key):
    """
    追加key，但要满足堆性质
    :param A:
    :param key:
    :return:
    """
    A.append(float("-inf"))
    heapIncreaseKey(A, len(A) - 1, key)


def heapDelete(A, i, heapSize):
    A[i] = A[heapSize - 1]
    maxHeapify(A, i, heapSize - 1)


if __name__ == "__main__":
    A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    buildMaxHeap(A)
    print(A)
    # sortByMaxHeap(A)
    # print(A)
    # print(heapMaximum(A))
    # print(extractHeapMaximum(A, len(A)))
    # print(A)
    #
    # maxHeapInsert(A, 100)
    # print(A)

    heapDelete(A, 2, len(A))
    print(A)
