# coding: utf-8
# Successful submition: 69802063

from typing import List, Any


class ScoreBoard:
    
    def __init__(self, name: str, score: int, penalty: int) -> None:
        self.name = name
        self.score = score
        self.penalty = penalty

    @property
    def key(self):
        return (-self.score, self.penalty, self.name)

    def __gt__(self, other) -> bool:
        return self.key > other.key

    def __lt__(self, other) -> bool:
        return self.key < other.key
    

def quicksort(a: List[Any], left: int, right: int) -> None:
    if left >= right:
        return -1
    pivot_idx = (left + right) // 2
    pivot = a[pivot_idx]
    l, r = left, right
   
    while l <= r:
        while a[l] < pivot:
            l += 1
        while a[r] > pivot:
            r -= 1
        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

    quicksort(a, left, r)
    quicksort(a, l, right)


if __name__ == "__main__":
    n = int(input())
    results = []
    for _ in range(n):
        name, score, penalty = input().strip().split()
        results.append(ScoreBoard(name, int(score), int(penalty)))
    quicksort(results, 0, n-1)
    for res in results:
        print(res.name)
