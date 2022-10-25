# coding: utf-8
# https://contest.yandex.ru/contest/25596/problems/C/?success=73024290#51450/2021_03_02/jI0XQTisPQ

from typing import List, Tuple

def greedy_gold(gold: List[Tuple[int]], capacity: int) -> int:
    gold.sort(key=lambda x: (x[0], x[1]))
    backpack = 0
    while capacity >= 0 and gold:
        cur_price, cur_kg = gold.pop()
        if cur_kg <= capacity:
            backpack += (cur_price * cur_kg)
        else:
            backpack += (cur_price * capacity)
        capacity -= cur_kg

    return backpack

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    data = []
    for _ in range(n):
        price, kilos = map(int, input().split())
        data.append((price, kilos))
    print(greedy_gold(data, m))