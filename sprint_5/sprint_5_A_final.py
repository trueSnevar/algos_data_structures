# coding: utf-8
# successful submition: 71236479

"""
-- ПРИНЦИП РАБОТЫ --
Задача сводится к реализации сортировки массива данных
с помощью двоичной кучи. Двочная куча представляет собой
(почти) полное двоичное дерево, где каждый дочерний узел
меньше своего родителя.

Сама куча представляет собой обычный массив с тем лишь 
дополнением, что первый элемент, он же максимальный
элемент кучи расположен по индексу 1, а индексы дочерних элементов
вычисляются по формулам i * 2, i*2+1 для левого и правого дочерних
узлов соответственно.

Алгоритм сортировки реализуется в два этапа:
    1) построение древовидного представления из полученного
       на вход массива данных;
    2) последовательного перемещения максимального элемента
       в конец исходного массива, при это поддерживая корректность
       самой кучи таким образом, что после обмена максимального элемента
       с последним неотсортированным элементом кучи, необходимо просеить 
       этот элемент вниз. В результате такого просеивания в корне кучи (элемент
       с индексом 1) оказался следующий по величине элемент.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Сначала для всех элементов входного массива строится корректная куча, что 
требует O(n) времени, но отрабатывает только 1 раз.
Каждая операция просеивания требует О(log n) времени, так как при просеивании
элемент сравнивается только с предками, а не с каждым элементом кучи.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Общая сложность алгоритма составляет O(n log(n)).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Дополнительная память не используется.
    Но поскольку в алгоритме есть рекурсивные вызовы для просеивания
    элементов, то в стеке вызовов может хранится до O(h) вызовов,
    где h - высота кучи.
"""

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

def max_heapify(data: List[Any], heap_size: int, idx: int) -> None:
    left = idx * 2
    right = idx * 2 + 1

    largest = idx

    if left < heap_size and data[left] > data[idx]:
        largest = left
    
    if right < heap_size and data[right] > data[largest]:
        largest = right
    
    if largest != idx:
        data[idx], data[largest] = data[largest], data[idx]
        max_heapify(data, heap_size, largest)

def build_max_heap(data: List[Any]):
    heap_size = len(data)

    for i in range(heap_size // 2, 0, -1):
        max_heapify(data, heap_size, i)

def heap_sort(data: List[Any]) -> None:
    build_max_heap(data)

    for i in range(len(data)-1, 1, -1):
        data[i], data[1] = data[1], data[i]
        max_heapify(data, i, 1)

if __name__ == "__main__":
    n = int(input())
    results = [None]
    for _ in range(n):
        name, score, penalty = input().strip().split()
        results.append(ScoreBoard(name, int(score), int(penalty)))
    heap_sort(results)
    for res in results[1:]:
        print(res.name)
