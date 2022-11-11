# coding: utf-8
# https://contest.yandex.ru/contest/26131/problems/K/?success=74469755#51450/2021_03_21/yqFARAEO3v

def compare_str(s1: str, s2: str):
    s1_l = []
    for i in s1:
        if ord(i) % 2 == 0:
            s1_l.append(i)

    s2_l = []

    for j in s2:
        if ord(j) % 2 == 0:
            s2_l.append(j)

    new_s1 = ''.join(s1_l)
    new_s2 = ''.join(s2_l)

    if new_s1 > new_s2:
        return 1
    elif new_s2 > new_s1:
        return -1
    else:
        return 0

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(compare_str(s1, s2))