# coding: utf-8
# https://contest.yandex.ru/contest/25069/problems?success=71399704#51450/2021_02_14/XoXatCklnC

def solution():
    v, e = map(int, input().split())
    graph = []
    for _ in range(v):
        lst = [0] * v
        graph.append(lst)
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1-1][v2-1] = 1
    for g in graph:
        print(*g, sep=' ')

if __name__ == "__main__":
    solution()