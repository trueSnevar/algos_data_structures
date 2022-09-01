# coding: utf-8

from typing import List

def conference_lovers(arr: List[int], k: int) -> List[int]:
    arr.sorted()
    max_val = arr[-1]
    counter = [0] * max_val

    for item in arr:
        max_val[item] += 1
