# coding: utf-8

import sys
sys.setrecursionlimit(100000)

from typing import List
T = 0

def main_dfs(start: int, graph: List[List[int]], vis, tin, tout):
    global T
    vis[start] = True
    tin[start] = T
    T += 1
    for v in graph[start]:
        if not vis[v]:
            main_dfs(v, graph, vis, tin, tout)
    tout[start] = T
    T += 1
        
if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1-1].append(v2-1)
    for i in range(v):
        graph[i].sort()
    enter = [None] * v
    leave = [None] * v
    visited = [False] * v
    main_dfs(0, graph, visited, enter, leave)
    for j in range(v):
        print(enter[j], leave[j])