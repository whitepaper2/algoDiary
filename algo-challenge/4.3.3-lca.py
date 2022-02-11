#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/02/11 14:15:53
@Author  : pengyuan.li
@File    : 4.3.3-lca.py
@Software: VSCode
'''

# here put the import lib
from collections import defaultdict
'''
求有根无向图两节点的公共父节点，与二叉树求公共父节点还是不同的。
'''


def lca(relations, root, u, v):
    """
    @param relations:图的边关系
    @param root:根节点
    @param u,v:待查询两节点
    @return : 
    """
    adj = defaultdict(list)
    vertex = set()
    
    def _init():
        for p,q in relations:
            adj[p].append(q)
            adj[q].append(p)
            vertex.add(p)
            vertex.add(q)
    _init()
    
    parent = dict()
    depth = dict()
    visited = {p:0 for p in vertex}
    def _dfs(node,nodeParent,nodeDepth):
        parent[node] = nodeParent
        depth[node] = nodeDepth
        visited[node] = 1
        for p in adj[node]:
            if visited[p]==0:
                _dfs(p,node,nodeDepth+1)
        
    _dfs(root,-1,0)

    while depth[u]>depth[v]:
        u = parent[u]
    while depth[u]<depth[v]:
        v = parent[v]
    while u!=v:
        u = parent[u]
        v = parent[v]

    return u


if __name__ == "__main__":
    relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [5, 7], [5, 8]]
    root = 1
    u, v = 5, 6
    print(lca(relations, root, u, v))

    u, v = 5, 2
    print(lca(relations, root, u, v))
