# -*- coding: utf-8 -*-
# https://contest.yandex.ru/contest/22779/problems/F/


class StackMax:
    """
    Нужно реализовать класс StackMax, 
    который поддерживает операцию определения максимума 
    среди всех элементов в стеке. 
    
    Класс должен поддерживать операции: 
    - push(x), где x – целое число, 
    - pop(), 
    - get_max();

    """
    def __init__(self):
        self.items = []

    def size(self):
         return len(self.items)

    def peek(self):
        return self.items[-1] 

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def get_max(self):
        return max(self.items)
        

my_stack = StackMax()

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'pop':
            if my_stack.size():
                my_stack.pop()
            else:
                print('error')
        if cmd[0] == 'push':
            my_stack.push(int(cmd[1]))
        if cmd[0] == 'get_max':
            if my_stack.size():
                print(my_stack.get_max())
            else:
                print('None')
