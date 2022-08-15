# -*- coding: utf-8 -*-
# https://contest.yandex.ru/contest/23638/problems/L?success=69671591#3484683/2020_11_16/hIKAEB0ETO

from typing import List, Tuple

def two_bicycles(days: List[int], price: int, left: int, right: int) -> Tuple[int]:
    """ Given the price of a bicycle, finds the first day
    when Vasya has enough money to buy it.
    
    """
    while left < right:
        mid = left + (right - left) // 2
        if days[mid] < price:
            left = mid + 1
        else:
            right = mid
    if left == right and days[left] >= price:
        return left+1
    return -1

if __name__ == "__main__":
    n = int(input())
    days = list(map(int, input().strip().split()))
    price = int(input())
    print(
        two_bicycles(days, price, 0, n-1), 
        two_bicycles(days, price*2, 0, n-1), 
        sep=" "
    )