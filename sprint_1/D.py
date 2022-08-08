from typing import List

def get_weather_randomness(ln: int, lst: List[int]) -> int:
    if ln == 1:
        return 1
    count = 0
    if lst[0] > lst[1]:
        count += 1
    if lst[-1] > lst[-2]:
        count += 1
    for i in range(1, ln-1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            count += 1
    return count

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return n, temperatures

n, temperatures = read_input()
print(get_weather_randomness(n, temperatures))