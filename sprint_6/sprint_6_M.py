# coding: utf-8
# https://contest.yandex.ru/contest/25069/problems/M/?success=72826110#51450/2021_02_14/gChWn6Yfpd

import sys
sys.setrecursionlimit(1000000)

def is_bigraph(graph):
    n = len(graph)
    colors = [0] * n
    visited = [False] * n

    def dfs(vtx, clr):
        visited[vtx] = True
        colors[vtx] = clr
        for to in graph[vtx]:
            if not visited[to]:
                if not dfs(to, 3 - clr):
                    return False
            else:
                if colors[to] == clr:
                    return False
        return True
    ans = True
    for i in range(n):
        if not visited[i]:
            ans &= dfs(i, 1)
    
    return ans
                
if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for i in range(e):
        f, t = map(int, input().split())
        graph[f-1].append(t-1)
        graph[t-1].append(f-1)
    res = is_bigraph(graph)
    print("YES" if res else "NO")