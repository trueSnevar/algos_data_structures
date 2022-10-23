# coding: utf-8
# https://contest.yandex.ru/contest/25069/problems/G/

from typing import List, Optional
from collections import deque

INF = float('inf')

def get_max_distance(graph: List[List[Optional[int]]], begin: int) -> List[int]:
    n = len(graph)
    visited = [False] * n
    distance = [INF] * n
    q = deque([begin])
    visited[begin] = True
    distance[begin] = 0
    while q:
        v_idx = q.pop()
        adj = graph[v_idx]
        for v in sorted(adj):
            if not visited[v]:
                distance[v] = distance[v_idx] + 1
                q.appendleft(v)
                visited[v] = True
    return max(distance[1:])

if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    t = int(input())
    print(get_max_distance(graph, t))