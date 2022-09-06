# coding: utf-8

import random
import string


base = 1000
mod = 123_987_123


def polynomial_hash(s: str, p: int, m: int) -> None:
    power_of_p = 1
    hash_val = 0

    for char in s:
        hash_val = ((hash_val + ord(char) * power_of_p) % m)
        power_of_p = (power_of_p * p) % m

    return hash_val


def solution():
    while True:
        s = ''.join(random.choice(letters) for i in range(20))
        hash_val = polynomial_hash(s[::-1], base, mod)
        if not mp.get(hash_val):
            mp[hash_val] = s
        else:
            print(s)
            print(mp[hash_val])
            break

if __name__ == "__main__":
    letters = string.ascii_lowercase
    s = ''.join(random.choice(letters) for i in range(10))
    hash_val = polynomial_hash(s[::-1], base, mod)
    mp = {}
    solution()