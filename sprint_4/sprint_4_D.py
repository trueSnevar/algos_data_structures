# coding: utf-8
# https://contest.yandex.ru/contest/23991/problems/D/?success=69907133#2989/2020_04_21/coNDFvzmdS

def get_classes(n: int) -> None:
    m = {}
    for _ in range(n):
        class_name = input().strip()
        if not m.get(class_name, False):
            print(class_name)
        m[class_name] = True
    return

if __name__ == "__main__":
    n = int(input())
    get_classes(n)