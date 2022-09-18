# coding: utf-8

from typing import List

def build_prefix_hash(base: int, mod: int, s: str) -> List[int]:
    prefix_hash = [0] 
    for char in s:
        hash_val = ((prefix_hash[-1] * base % mod) + ord(char)) % mod
        prefix_hash.append(hash_val)
    return prefix_hash

def get_powers(base: int, mod: int, s: str) -> List[int]:
    powers = [1]
    for i in range(1, len(s)+1):
        power = (powers[i-1] * base) % mod
        powers.append(power)
    return powers

def get_prefix_hash(mod: int, left: int, right: int, prefix: List[int], powers: List[int]) -> int:
    return (prefix[right] + mod - (prefix[left] * powers[right - left]) % mod) % mod

if __name__ == "__main__":
    k = int(input())
    m = int(input())
    s = input().strip()
    ph = build_prefix_hash(k, m, s)
    pw = get_powers(k, m, s)
    r = int(input())
    for _ in range(r):
        l, r = tuple(map(int, input().split()))
        print(get_prefix_hash(m, l-1, r, ph, pw))