# coding: utf-8

def get_hash(s: str, mod: int, a: int) -> int:
    n = len(s)
    res = 0
    for c in s:
        res += ((ord(c) * a**(n-1))) % mod
        n -= 1
    
    return res % mod


if __name__ == "__main__":
    a = int(input())
    mod = int(input())
    s = input()
    print(get_hash(s, mod, a))