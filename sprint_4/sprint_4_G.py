# coding: utf-8
# doesn't work

from typing import List


def competitions(n: int, arr: List[int]) -> int:
    m = {1: 0, 0: 0}
    best = 0
    cur = 0
    for num in arr:
        cur += 1
        m[num] += 1
        if m[0] == m[1]:
            best = max(best, cur)
            cur = 0
    return best

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(competitions(n, arr))