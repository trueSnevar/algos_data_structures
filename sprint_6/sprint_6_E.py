# coding: utf-8
# https://contest.yandex.ru/contest/25069/problems/E/?success=71903498#51450/2020_08_11/9WmDHlxND4

def linked_components(graph):
    visited = [False] * len(graph)
    # cnt = 0
    components = []
    stack = []
    for i in range(1, len(graph)):
        if visited[i]:
            continue
        # cnt += 1
        visited[i] = True
        component = []
        stack = [i]
        while stack:
            vtx = stack.pop()
            component.append(vtx)
            for v in graph[vtx]:
                if not visited[v]:
                    stack.append(v)
                    visited[v] = True
        components.append(component)
    return components

if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    res = linked_components(graph)
    print(len(res))
    for lst in res:
        print(*sorted(lst), sep=' ')