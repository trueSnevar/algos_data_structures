# coding: utf-8
# https://contest.yandex.ru/contest/26131/problems/D/?success=75252088#51450/2020_07_20/qkQw8EnIGk

from typing import List

def longest_common_prefix(strs: List[str]) -> int:
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return len(res)
        res += strs[0][i]

    return len(res)

if __name__ == "__main__":
    n = int(input())
    data = list(input() for _ in range(n))
    print(longest_common_prefix(data))
