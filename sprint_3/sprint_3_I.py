# coding: utf-8
# https://contest.yandex.ru/contest/23638/problems/I/?success=69942044#2989/2020_04_13/QUOg7a2HDC

from typing import List

def conference_lovers(arr: List[int], k: int) -> List[int]:
    m = {}
    for el in arr:
        if el in m:
            m[el] += 1
        else:
            m[el] = 1
    srt = [(k,v) for k,v in m.items()]
    srt.sort(key=lambda x: (-x[1], x[0]))
    res = [k for k,v in srt]   
    return res[:k]

if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().strip().split()))
    k = int(input())
    print(*conference_lovers(lst, k))