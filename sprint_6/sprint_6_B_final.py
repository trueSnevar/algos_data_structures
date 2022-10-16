# coding: utf-8
# successful submission: 72196137

"""
ПРИНЦИП РАБОТЫ
    Если представить, что города это вершины графа, 
    а железные дороги - это ребра, соединяющие вершины,
    то задача сведется к поиску цикла в графе. То есть если цикл в
    графе обнаружен, это значит, что карта железных дорог составлена
    неоптимально, то есть из одной вершины в другую можно попасть,
    используя оба типа дорог.

    Для определения наличия цикла применяется цветовая раскраска вершин:
        1) Белая вершина - не посещена;
        2) Серая вершина - посещена, но не все смежные вершины обработаны;
        3) Черная вершина - посещена, и все смежные вершины обработаны.

    Следовательно, если в процессе обхода графа встретится вершина
    с серым цветом, то цикл найден.
ВРЕМЕННАЯ СЛОЖНОСТЬ
    O(V+E) - где V - количество вершин, а Е - количество ребер в графе.
ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Если не считать сам граф, который нужно хранить, то потребуется О(V)
    дополнительной памяти для хранения списка цветов вершин.
"""


from typing import List

def is_cyclic(graph: List[List[int]]) -> bool:
    colors = ['white'] * len(graph)

    def dfs(vtx: int) -> bool:
        stack = [vtx]
        while stack:
            v = stack.pop()
            if colors[v] == 'white':
                colors[v] = 'gray'
                stack.append(v)
                for adj in graph[v]:
                    if colors[adj] == 'gray':
                        return True
                    elif colors[adj] == 'white':
                        stack.append(adj)
            elif colors[v] == 'gray':
                colors[v] = 'black'
        return False

    for i in range(len(graph)):
        if colors[i] == 'white':
            if dfs(i):
                return True
    return False

if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        map = input().strip()
        for j, t in enumerate(map):
            if t == "B":
                graph[i].append(i+j+1)
            elif t == "R":
                graph[i+j+1].append(i)
    res = is_cyclic(graph)
    print("NO" if res else "YES")