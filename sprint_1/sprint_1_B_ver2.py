# successful submition: 69526060

from typing import List

def sleight_of_hand(k: int, grid: List[str]) -> int:
    rounds = '123456789'
    grid_count = {r:0 for r in rounds}
    for item in grid:
        if item in rounds:
            grid_count[item] += 1
    fingers = 2*k
    final_score = 0
    for num in rounds:
        if grid_count[num] > 0 and grid_count[num] <= fingers:
            final_score += 1
    return final_score


if __name__ == '__main__':
    k = int(input())
    grid = []
    for i in range(4):
        grid += input()
    print(sleight_of_hand(k, grid))