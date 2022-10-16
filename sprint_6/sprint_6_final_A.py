# coding: utf-8
# Successfull sumbition: 72188143

"""
"""

import heapq

from collections import defaultdict
from typing import DefaultDict, List, Optional, Tuple

def max_spanning_tree(graph: DefaultDict[int, List[Optional[Tuple[int, int, int]]]], start: int = 1) -> Tuple[List[bool], int]:
    unvisited = list(graph.keys())
    visited = [False] * (len(graph) + 1)
    total_cost = 0

    unvisited.remove(start)
    visited[start] = True

    heap = graph[start]
    heapq.heapify(heap)

    while unvisited and heap:
        (cost, n2, n1) = heapq.heappop(heap)
        new_node = None

        if n1 in unvisited and visited[n2]:
            new_node = n1

        elif visited[n1] and n2 in unvisited:
            new_node = n2

        if new_node != None:
            unvisited.remove(new_node)
            visited[new_node] = True
            total_cost += abs(cost)

            for node in graph[new_node]:
                heapq.heappush(heap, node)

    return visited[1:], total_cost


if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = defaultdict(list)
    for i in range(1, v+1):
        graph[i]
    for _ in range(e):
        v1, v2, w = map(int, input().split())
        graph[v1].append((-w, v2, v1))
        graph[v2].append((-w, v1, v2))
    visited, total = max_spanning_tree(graph)
    print(total if all(visited) else "Oops! I did it again")