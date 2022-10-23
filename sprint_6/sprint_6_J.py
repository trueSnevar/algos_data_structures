# coding: utf-8

def main_top_sort(graph):
    order = []
    visited = [False] * len(graph)

    def ts(v):
        visited[v] = True
        for vtx in graph[v]:
            if not visited[vtx]:
                ts(vtx)
        order.append(v+1)
    
    for i in range(len(graph)):
        if not visited[i]:
            ts(i)
    return order


if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1-1].append(v2-1)
    for i in range(v):
        graph[i].sort()
    res = main_top_sort(graph)
    res.reverse()
    print(*res)

# coding: utf-8

# def dfs(v, used, graph, topsort):
# 	used[v] = 1
# 	for to in graph[v]:
# 		if used[to] == 0:
# 			dfs(to, used, graph, topsort)
# 	topsort.append(v+1)
# 	used[v] = 2

# def read_oriented_graph():
# 	n, m = map(int, input().split())
# 	graph = [[] for _ in range(n)]
# 	for i in range(m):
# 		u, v = map(int, input().split())
# 		graph[u-1].append(v-1)
# 	return graph, n
             

# topsort = []
# g, n = read_oriented_graph()
# used = [0 for _ in range(n)]
# for v in range(n):
# 	if used[v] == 0:
# 		dfs(v, used, g, topsort)
# topsort.reverse()
# print(*topsort)