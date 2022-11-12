# coding: utf-8

from typing import List

def prefix_func(s: str) -> List[int]:
    n = [0] + [None] * (len(s) - 1)

    for i in range(1, len(s)):
        k = n[i - 1]
        while (k > 0) and (s[k] != s[i]):
            k = n[k - 1]
        if s[k] == s[i]:
            k += 1

        n[i] = k

    return n

if __name__ == "__main__":
    s = input()
    print(*prefix_func(s))