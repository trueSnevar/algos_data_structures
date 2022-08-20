# -*- coding: utf-8 -*-
# https://contest.yandex.ru/contest/22779/problems/L/

def fib(n: int, k: int) -> int:
    """ Вывести k последних
    цифр числа n Фибоначчи.
     
    Чтобы вычислить k последних цифр некоторого числа x, 
    достаточно взять остаток от его деления на число 10k 
    """
    n0 = 0
    n1 = 1
    for _ in range(n):
        n0, n1 = n1, (n0 + n1) % (10**k)
    return n1

if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    print(fib(n, k))
