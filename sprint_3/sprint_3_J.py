# -*- coding: utf-8 -*-

from typing import List

SWAP_FLAG = False

def bubble_sort(lst: List[int]) -> None:
    sorted = False
    global SWAP_FLAG
    while not sorted:
        sorted = True
        for idx in range(len(lst)-1):
            if lst[idx] > lst[idx+1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                sorted = False
                SWAP_FLAG = True
        if not sorted:
            print(*lst, sep=' ')
    return lst

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    bubble_sort(arr)
    if not SWAP_FLAG:
        print(*arr)