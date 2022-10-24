# coding: utf-8
# https://contest.yandex.ru/contest/25596/problems/B/?success=72936130#2989/2020_04_29/JbNm0VNE65

from typing import List, Tuple

def timetable(classes: List[Tuple[float]]):
    classes.sort(key=lambda x: (x[1], x[0]))
    res = [classes[0]]
    for item in classes[1:]:
        prev = res[-1]
        if prev[1] <= item[0]:
            res.append(item)
    return res

if __name__ == "__main__":
    n = int(input())
    data = []
    for _ in range(n):
        b, e = map(float, input().split())
        data.append((b, e))
    ans = timetable(data)
    print(len(ans))
    for i in ans:
        print(*i)