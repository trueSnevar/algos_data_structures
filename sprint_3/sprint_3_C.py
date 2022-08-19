# coding: utf-8
# https://contest.yandex.ru/contest/23638/problems/C/?success=69704991#2989/2020_04_29/l8CwSaKkIK

def is_substring(s: str, t: str) -> bool:
    sp, tp = 0, 0

    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1

    if sp == len(s):
        return True
    return False

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(is_substring(s,t))

