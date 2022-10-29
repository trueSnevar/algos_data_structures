# coding: utf-8
# https://contest.yandex.ru/contest/25596/problems/H/?success=73300510#51450/2020_08_28/g5cpJnV9Rk

from typing import List


def flower_field(points: List[List[int]], n: int, m: int) -> int:
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + points[i][j]
    return dp[n-1][m-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    mtx = []
    for _ in range(n):
        row = [int(x) for x in input()]
        mtx.insert(0, row)
    print(flower_field(mtx, n, m))
