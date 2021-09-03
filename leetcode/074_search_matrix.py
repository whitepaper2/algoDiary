#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午3:23
# @Author  : pengyuan.li
# @Site    : 
# @File    : 074_search_matrix.py
# @Software: PyCharm

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    note:二维矩阵转为一维，再使用二分查找法
    :param matrix:
    :param target:
    :return:
    """
    len_of_matrix = len(matrix)
    new_matrix = []
    for i in range(len_of_matrix):
        for j in range(len(matrix[i])):
            new_matrix.append(matrix[i][j])
    len_of_newmatrix = len(new_matrix)
    left = 0
    right = len_of_newmatrix
    while left <= right:
        mid = left + (right - left) // 2
        if new_matrix[mid] == target:
            return True
        elif new_matrix[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def searchMatrix2(matrix: List[List[int]], target: int) -> bool:
    # 观察数据特性，每行最后一个数字与目标值比较，如果大于目标值，则目标值可能在该行，再使用二分法判断；否则在下一行继续判断。
    len_of_matrix = len(matrix)
    i = 0
    while i < len_of_matrix:
        len_imatrix = len(matrix[i])
        if len_imatrix > 0:
            if matrix[i][len_imatrix - 1] < target:
                i = i + 1
            elif matrix[i][len_imatrix - 1] == target:
                return True
            else:
                break
        else:
            i = i + 1
    if i == len_of_matrix:
        return False
    len_of_newmatrix = len(matrix[i])
    left = 0
    right = len_of_newmatrix
    while left <= right:
        mid = left + (right - left) // 2
        if matrix[i][mid] == target:
            return True
        elif matrix[i][mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def searchMatrix3(matrix: List[List[int]], target: int) -> bool:
    """
    note:双指针法
    :param matrix:
    :param target:
    :return:
    """
    m = len(matrix)
    n = len(matrix[0])
    row = 0
    col = n - 1
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col = col - 1
        else:
            row = row + 1
    return False


def searchMatrix4(matrix: List[List[int]], target: int) -> bool:
    """
    note:不需另存一维数据，坐标变换，再应用二分查找法
    :param matrix:
    :param target:
    :return:
    """
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n
    while left < right:
        mid = left + (right - left) // 2
        if matrix[mid // n][mid % n] == target:
            return True
        elif matrix[mid // n][mid % n] > target:
            right = mid
        else:
            left = mid + 1
    return False


if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    print(searchMatrix4(matrix, target))

    target = 13
    print(searchMatrix4(matrix, target))

    matrix = [[]]
    target = 3
    print(searchMatrix4(matrix, target))
