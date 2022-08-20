# -*- coding: utf-8 -*-
# https://contest.yandex.ru/contest/22779/problems/G/


class StackMax:
    """
    Реализовать StackMaxEffective, поддерживающий операцию 
    определения максимума среди элементов в стеке. 
    
    Сложность операции должна быть O(1). Для пустого стека возвращать None. 
    При этом push(x) и pop() также должны выполняться за константное время.
    """
    def __init__(self):
        self.items = []

    def size(self):
         return len(self.items)

    def peek(self):
        return self.items[-1][0] 

    def push(self, x):
        if self.size():
            curr_max = self.items[-1][1]
            max_item = max(curr_max, x)
        else:
            max_item = x
        self.items.append((x, max_item))


    def pop(self):
        return self.items.pop()[0]

    def get_max(self):
        return self.items[-1][1]
        

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
