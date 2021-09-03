#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 下午5:50
# @Author  : pengyuan.li
# @Site    : 
# @File    : 022_generate_parenthesis.py
# @Software: PyCharm


def generate_parenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []

    def generate_dfs(left, right, out, res):
        """
        深度优先遍历
        :param left:剩余的"("的个数
        :param right: 剩余的")"的个数
        :param out: 当前存储的结果
        :param res: 符合条件的总结果
        :return:
        """
        if left > right:
            return
        if left == 0 and right == 0:
            res.append(out)
        else:
            if left > 0:
                generate_dfs(left - 1, right, out + "(", res)
            if right > 0:
                generate_dfs(left, right - 1, out + ")", res)

    generate_dfs(n, n, "", res)
    return res


if __name__ == "__main__":
    n = 3
    print(generate_parenthesis(n))
