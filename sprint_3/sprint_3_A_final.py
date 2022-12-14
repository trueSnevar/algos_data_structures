# coding: utf-8
# Successful submition: 69752689

"""
-- ПРИНЦИП РАБОТЫ --
Задача решается двоичным поиском с тем отличием
от стандартного, что входной массив имеет точку перелома,
то есть левая часть массива больше, чем правая.
В этом случае после нахождения элемента в середине массива,
нужно произвести дополнительную проверку, чтобы продолжить
поиск нужного элемента в правильной части массива.

Так, если элемент в середине больше (либо равен), чем текущий левый элемент, 
то решение сводится к стандартному двоичному поиску. 

Если же элемент в середине меньше, чем текущий левый элемент, значит 
мы находимся в части после точки перелома, и нужно проверить, находится
ли искомый элемент в интервале значений от середины, до текущего правого элемента,
и если нет, то поиск необходимо продолжить в левой части массива.

Решение унифицировано как для массива, отсортированного по возрастанию,
так и для массива с точкой перелома.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Несмотря на то, что порядок элементов в массиве
нарушен, мы все равно имеем две отсортированные
по возрастанию половины, а значит можем применять
двоичный поиск для каждой из половин массива, нужно
лишь произвести дополнительную проверку и определить
ту половину массива, в которой продолжить поиск.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
На каждой итерации входной массив делится пополам, поэтому
временная сложность О(log(n))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Дополнительная память не используется, поэтому
пространственная сложность = О(1).
"""

from typing import List

def broken_search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r-l) // 2
        if nums[mid] == target:
            return mid
        elif nums[l] <= nums[mid]:
            if nums[l] <= target and nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1 
        else:
            if nums[mid] < target and nums[r] >= target:
                l = mid + 1
            else:
                r = mid - 1
    return -1 



def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr2 = [4,5,6,7,0,1,2]
    assert broken_search(arr2, 3) == -1
    arr3 = [1]
    assert broken_search(arr3, 0) == -1

if __name__ == "__main__":
    test()