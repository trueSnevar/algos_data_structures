# coding: utf-8

from typing import List

MOD = 10**9 + 7

def climbing_stairs(n: int, m: int) -> int:
    stairs = [1]  # index = 0
    for _ in range(n):
        stairs.append(sum(stairs) % MOD)
        if len(stairs) > m:
            stairs.pop(0)
    if len(stairs) > 1:
        return stairs[-2]
    else:
        return stairs[-1]

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(climbing_stairs(n, k))
