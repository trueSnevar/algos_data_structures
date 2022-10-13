# coding: utf-8
# https://contest.yandex.ru/contest/25069/problems/D/

from typing import List, Optional
from collections import deque

def bfs(begin: int, graph: List[List[Optional[int]]]) -> List[int]:
    visited = [False] * len(graph)
    q = deque([begin])
    visited[begin] = True
    res = []
    while q:
        v_idx = q.pop()
        res.append(v_idx)
        adj = graph[v_idx]
        for v in sorted(adj):
            if not visited[v]:
                q.appendleft(v)
                visited[v] = True
    return res


if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    start: int = int(input())
    res = bfs(start, graph)
    print(*res, sep=' ')