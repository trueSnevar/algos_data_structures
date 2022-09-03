# coding: utf-8
# https://contest.yandex.ru/contest/23638/problems/P/?success=69946787#3484683/2020_05_28/FIitHMHygh

from typing import List

def part_sort(arr: List[int], ln: int) -> int:
    """ Нужно хранить максимальный элемент 
    в текущем блоке и завершать блок, если индекс
    будет равным текущиму максимальному элементу:

        блок 1   |б.2 | б.3
    [3, 2, 0, 1, | 4, | 6, 5].
                 |    |

    Если элемент совпал с индексом, то он на своем месте,
    и считаем его отдельным блоком.             
    """
    max_block = -1
    counter = 0
    for i in range(ln):
        max_block = max(max_block, arr[i])
        if max_block == i:
            counter += 1
    return counter

if __name__ == "__main__":
    n: int = int(input())
    lst: List[int] = list(map(int, input().strip().split()))
    print(part_sort(lst, n))