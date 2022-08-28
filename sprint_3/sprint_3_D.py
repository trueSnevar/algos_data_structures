# coding: utf-8
# https://contest.yandex.ru/contest/23638/problems/D/?success=69821310#2989/2020_04_29/72BUTYqfVz

from typing import List

def cookies(greedy: List[int], sizes: List[int], g_len: int, s_len: int) -> int:

    greedy.sort()
    sizes.sort()
    count = 0
    g = g_len - 1
    s = s_len - 1
    while g >= 0 and s >= 0:
        if greedy[g] <= sizes[s]:
            count += 1
            sizes.pop()
            g -= 1
            s -= 1
        else:
            g -= 1
    return count
    

if __name__ == "__main__":
    n = int(input())
    greedy = list(map(int, input().strip().split()))

    m = int(input())
    sizes = list(map(int, input().strip().split()))
    print(cookies(greedy, sizes, n, m))
    
