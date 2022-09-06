# coding: utf-8
# https://contest.yandex.ru/contest/23991/problems/A/?success=70065230#51450/2020_07_09/ggPyaEPG8k

def polynomial_hash(s: str, p: int, m: int) -> int:
    power_of_p = 1
    hash_val = 0

    for char in s:
        hash_val = ((hash_val + ord(char) * power_of_p) % m)
        power_of_p = (power_of_p * p) % m
 
    return hash_val

if __name__ == "__main__":
    base = int(input())
    mod = int(input())
    string = input()    
    print(polynomial_hash(string[::-1], base, mod))