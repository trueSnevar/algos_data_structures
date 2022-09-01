# coding: utf-8

from typing import List

def get_second_diff(ln: int, arr: List[int], k: int) -> int:
    diffs = []
    for i in range(ln-1):
        for j in range(i+1, ln):
            cur_diff = abs(arr[i] - arr[j])
            diffs.append(cur_diff)
    diffs.sort()
    return diffs[k-1]



if __name__ == "__main__":
    n = int(input())
    islands = list(map(int, input().strip().split()))
    idx = int(input())
    print(get_second_diff(n, islands, idx))