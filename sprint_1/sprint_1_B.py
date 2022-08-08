# successful submition: 69519403

from typing import List, Tuple

def sleight_of_hand(k: int, grid: List[str]) -> int:
    score = 0
    for round in range(10):
        num = 0
        for item in grid:
            if str(round) in item:
                num += item.count(str(round))
        if num > 0 and num <= (2*k):
            score += 1
    return score

def read_input() -> Tuple[int, List[str]]:
    k = int(input())
    grid = []
    for i in range(4):
        grid.append(input().strip())
    return k, grid

k, grid = read_input()
print(sleight_of_hand(k, grid))