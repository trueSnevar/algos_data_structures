# coding: utf-8
# https://contest.yandex.ru/contest/23991/problems/E/?success=70017689#2989/2020_04_21/PHfYqqL8FT
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/


def substring(s: str) -> int:
    m = {}
    left = 0
    best = 0
    for idx, char in enumerate(s):
        if char in m and left <= m[char]:
           left = m[char] + 1
        else:
            best = max(best, idx - left + 1)
        m[char] = idx
    return best

if __name__ == "__main__":
    s = input().strip()
    print(substring(s))