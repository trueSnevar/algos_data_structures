# coding: utf-8
# Successfull sumbition: 72188143

"""
ПРИНЦИП РАБОТЫ
    Для решения задачи поиска максимального остового дерева
    воспользуемся алгоритмом Прима с на очереди с приоритетом.
    Кучу мы, конечно же, сами реализовывать не будем, а воспользуемся
    встроенной структурой данных. Проблема в том, что встроенная куча
    является минимальной, то есть такой кучей, где в корне лежит минимальный
    элемент, а нам требуется максимальный. Проблема решается просто - достаточно
    вес ребра графа сделать отрицательным.

    Сначала берётся произвольная вершина и находится ребро, инцидентное данной вершине
    и обладающее наименьшей стоимостью. Найденное ребро и соединяемые им две вершины образуют дерево. 
    Затем, рассматриваются рёбра графа, один конец которых — уже принадлежащая дереву вершина, 
    а другой — нет; из этих рёбер выбирается ребро наименьшей (в нашем случае - наибольшей) стоимости. 
    Выбираемое на каждом шаге ребро присоединяется к дереву. 
    Рост дерева происходит до тех пор, пока не будут исчерпаны все вершины исходного графа.

    https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9F%D1%80%D0%B8%D0%BC%D0%B0

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Использование очереди с приоритетом позволяет сократить время поиска
    остовного дерева максимальной стоимости до О(E*log(V)), где E - кол-во ребер,
    а V - кол-во вершин.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Хранение кучи потребует кол-во памяти, равное кол-ву вершин - О(V).
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