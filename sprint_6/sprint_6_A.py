# coding: utf-8
# https://contest.yandex.ru/contest/25069/problems?success=71399704#51450/2021_02_14/XoXatCklnC

def solution():
    v, e = map(int, input().split())
    graph = [0] * (v+1)
    for _ in range(e):
        v1, v2 = map(int, input().split())
        if not graph[v1]:
            graph[v1] = [1, v2]
        else:
            graph[v1][0] += 1
            graph[v1].append(v2)
    for g in graph[1:]:
        if g:
            print(*g, sep=' ')
        else:
            print(g)

if __name__ == "__main__":
    solution()