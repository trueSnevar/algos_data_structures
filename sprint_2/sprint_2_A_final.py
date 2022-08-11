# -*- coding: utf-8 -*-
# successful submission: 69639630

"""
-- ПРИНЦИП РАБОТЫ --
Я реализовал очередь c двумя концами, то есть элементы можно
как добавлять, так и получать с обоих концов очереди.
В реализации двусторонней очереди я использовал кольцевой буффер,
что позволяет ограничить размер очереди n элементами.


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Реализация двусторонней очереди сделана
с помощью списка (class List), который позволяет
присваивать и получать значения по индексу, а значит
если применить метод двух указателей - на начало и конец
очереди, то появится возможность добавлять и получать элементы
с обоих концов.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
В требованиях к реализации указано, что все операции
по добавлению и извлечению элементов требуется выполнять
за константное (О(1)) время.

Поскольку для хранения элементов в очереди 
используется стандартный список (class List),
у которого получение элемента по индексу, и присваивание значения
по индексу осуществляется за константоное время, 
все операции в двусторонней очереди будут также выполняться
за константное время.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Данная реализация двусторонней очереди имеет
ограниченный размер в качестве входного параметра,
то есть способна хранить максимум заранее определенное
кол-во элементов. То есть в худшем случае очередь будет
занимать О(n) памяти.
"""

from typing import Optional

class MyDeque:
    """ The class provides 
    a custom double-ended queue 
    using circular buffer.

    """
    def __init__(self, n: int) -> None:
        self.deque = [None] * n
        self.max_size = n
        self.head = 0
        self.tail = -1
        self.cur_size = 0

    @property
    def is_full(self) -> bool:
        return self.cur_size == self.max_size
    
    @property
    def is_empty(self) -> bool:
        return self.cur_size == 0

    def push_back(self, value: int) -> None:
        """
        Adds a value to the right end 
        of the deque.

        """
        if not self.is_full:
            self.tail = (self.tail + 1) % self.max_size
            self.deque[self.tail] = value
            self.cur_size += 1 

    def push_front(self, value: int) -> None:
        """
        Adds a value to the left end 
        of the deque.
        
        """
        if not self.is_full:
            self.head = (self.head - 1) % self.max_size
            self.deque[self.head] = value
            self.cur_size += 1

    def pop_back(self) -> Optional[int]:
        """
        Retreives value from the right
        end of the deque.

        """
        if self.is_empty:
            return None
        val = self.deque[self.tail]
        self.deque[self.tail] = None
        self.tail = (self.tail - 1) % self.max_size        
        self.cur_size -= 1
        return val

    def pop_front(self) -> Optional[int]:
        """
        Retreives value from the left
        end of the deque.

        """
        if self.is_empty:
            return None
        val = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.cur_size -= 1
        return val

if __name__ == "__main__":
    cmd_num = int(input())
    max_size = int(input())
    dq = MyDeque(max_size)
    for _ in range(cmd_num):
        cmd = input().split(' ')
        if cmd[0] == 'push_back':
            if dq.is_full:
                print('error')
            else:
                dq.push_back(int(cmd[1]))
        if cmd[0] == 'push_front':
            if dq.is_full:
                print('error')
            else:
                dq.push_front(int(cmd[1]))
        if cmd[0] == 'pop_back':
            if dq.is_empty:
                print('error')
            else:
                print(dq.pop_back())
        if cmd[0] == 'pop_front':
            if dq.is_empty:
                print('error')
            else:
                print(dq.pop_front())


        
