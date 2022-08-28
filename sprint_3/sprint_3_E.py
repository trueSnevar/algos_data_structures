# coding: utf-8
# https://contest.yandex.ru/contest/23638/problems/E/?success=69821319#2989/2020_04_29/2RCY8PqnPM

from typing import List

def buy_houses(money: int, prices: List[int]) -> int:
    prices.sort()
    counter = 0
    while money >= 0:
        for price in prices:
            diff = money - price
            if diff >= 0:
                counter += 1
            money -= price
    return counter

if __name__ == "__main__":
    n, money = input().strip().split()
    prices = list(map(int, input().strip().split()))
    print(buy_houses(int(money), prices))