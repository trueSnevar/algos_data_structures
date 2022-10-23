# coding: utf-8

from typing import List

def max_profit(lst: List[int]) -> int:
    l = 0
    r = 1
    res = 0
    cur = 0
    while r < (len(lst)):
        diff = lst[r] - lst[l]
        if diff > 0 and diff > cur:
            cur = diff
            r += 1
        else:
            l = r
            r = l + 1
            res += cur
            cur = 0
    res += cur
    return res 

if __name__ == "__main__":
    n = int(input())

    data = list(map(int, input().strip().split()))
    print(max_profit(data))