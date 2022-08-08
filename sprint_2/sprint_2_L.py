# -*- coding: utf-8 -*-

def fib(n, k):
    n0 = 0
    n1 = 1
    for _ in range(n):
        n0, n1 = n1, (n0 + n1) % (10**k)
    return n1

if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    print(fib(n, k))
