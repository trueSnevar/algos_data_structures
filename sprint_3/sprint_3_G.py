# coding: utf-8
# https://contest.yandex.ru/contest/23638/problems/G/?success=69740930#3484683/2020_05_28/ZnyHg7m0F7

import sys
from typing import List

def wardrobe(lst: List[int], k: int) -> List[int]:
    """ Implements counting sort of an input array.

    An array that specifies the color for each item. 
    Pink is marked 0 , yellow is 1 , crimson is 2 . 

    Args:
      lst:
        A list of integers.
      k:
        the number of items in the wardrobe, 
        it does not exceed 1000000.
    
    Returns:
        output the list of colors 
        in the correct order 
    
    Example:
        input: 7
               0 2 1 2 0 0 1
        output: 0 0 0 1 1 2 2
    """
    count = [0] * 3
    for elem in lst:
        count[elem] += 1
    index = 0
    for i in range(len(count)):
        for _ in range(1, count[i]+1):
            lst[index] = i
            index += 1
    return lst

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    #print(*wardrobe(arr, n))
    res = wardrobe(arr,n)
    sys.stdout.write(
        " ".join(map(str, res)) + "\n"
    )