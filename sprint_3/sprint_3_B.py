# -*- coding: utf-8 -*-
# https://contest.yandex.ru/contest/23638/problems/B/?success=69941038#2989/2020_04_14/RkGbWqMPoA

from typing import List

MAPPING = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz' 
}

def make_combinations(code: str) -> List[str]:
    res = ['']

    for char in code:
        cur_seq = MAPPING[char]
        res = [prefix + letter for prefix in res for letter in cur_seq]
    return res


if __name__ == "__main__":
    s = input().strip()
    print(*make_combinations(s))