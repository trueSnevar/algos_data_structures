# coding: utf-8

from typing import List

def triangle_perimeter(arr: List[int]) -> int:
    arr.sort(reverse=True)
    best = 0
    for i in range(len(arr)-2):
        c, b, a = arr[i:i+3]
        if c < b + a:
            s = sum((c,b,a))
            best = max(best, s)
    return best

if __name__ == "__main__":
    n = int(input())
    lns = list(map(int, input().strip().split()))
    print(triangle_perimeter(lns))