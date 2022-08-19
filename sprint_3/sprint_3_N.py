# coding: utf-8
# https://contest.yandex.ru/contest/23638/problems/N/?success=69704784#3484683/2020_05_28/2eFko4Jefr

from typing import List, Tuple

def get_flower_pods(beds: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    beds = sorted(beds, key=lambda b: b[0])
    res = [beds[0]]
    for cur_bed in beds:
        last_added = res[-1]
        if last_added[1] < cur_bed[0]:
            res.append(cur_bed)
        else:
            res[-1] = (last_added[0], max(last_added[1], cur_bed[1]))
    return res

if __name__ == "__main__":
    n: int = int(input())
    beds = [None] * n
    for i in range(n):
        bed = tuple(map(int, input().strip().split()))
        beds[i] = bed
    res = get_flower_pods(beds)
    for item in res:
        print(*item, sep=" ")

    