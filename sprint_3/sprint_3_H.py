# -*- coding: utf-8 -*-
# https://contest.yandex.ru/contest/23638/problems/H?success=69697360#3484683/2020_06_11/QOZdNxLp7y

from typing import List

def insertion_key_sort(lst: List[str], key) -> str:
    for i in range(1, len(lst)):
        item_to_insert = lst[i]
        j = i
        while j > 0 and key(item_to_insert, lst[j-1]):
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = item_to_insert
    lst.reverse()
    return "".join(lst)

def compare_str(a: str, b: str) -> bool:
    a_num: int = int(a) * 10**len(b) + int(b)
    b_num: int = int(b) * 10**len(a) + int(a)
    # just change comparison sing 
    # to sort in descending order
    return a_num < b_num

if __name__ == "__main__":
    n: int = int(input())
    data: List[str] = input().strip().split()
    print(insertion_key_sort(data, compare_str))
