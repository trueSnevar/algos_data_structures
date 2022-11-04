# coding: utf-8
# Successful submission: 73782210

from typing import List

def points_partition(points: List[int]) -> bool:
    
    total = sum(points)
    if total % 2 != 0:
        return False
    target = total // 2

    dp = [True] + [False] * (target)
    for point in points:
        for j in range(target, point - 1, -1):
            dp[j] = dp[j] or dp[j - point]

    return dp[target]


if __name__ == "__main__":
    n = int(input())
    data: List[int] = list(map(int, input().split()))
    print(points_partition(data))
