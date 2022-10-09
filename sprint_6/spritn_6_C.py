# coding: utf-8

from typing import List

def main_dfs(start_vtx: int, graph: List[List[int]]):
    visited = set()
    res = []
    stack = [start_vtx]
    while stack:
        vtx = stack.pop()
        if vtx not in visited:
            visited.add(vtx)
            res.append(vtx)
            nxt = graph[vtx-1]
            if nxt != 0:
                stack.extend(reversed(sorted(nxt)))
    return res
        
if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [0] * v
    for _ in range(e):
        v1, v2 = map(int, input().split())
        if not graph[v1-1]:
            graph[v1-1] = [v2]
        else:
            graph[v1-1].append(v2)
        if not graph[v2-1]:
            graph[v2-1] = [v1]
        else:
            graph[v2-1].append(v1)
    begin = int(input())
    res = main_dfs(begin, graph)
    print(*res, sep=' ')