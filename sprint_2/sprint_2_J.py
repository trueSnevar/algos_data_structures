# coding: utf-8
# https://contest.yandex.ru/contest/22779/problems/I/


class ListNode:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class ListQueue:
    """ Класс, реализующий
    ограниченную очередь на связном списке.
    
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current_size = 0

    def get(self):
        if self.current_size == 0:
            return
        temp = self.head
        self.head = temp.next
        self.current_size -= 1

        if self.head == None:
            self.tail = None      

    def put(self, val):
        temp = ListNode(val)
        self.current_size += 1
        if self.tail == None:
            self.head = self.tail = temp
            return
        # кладем элемент в следующий за 
        # хвостом нод
        self.tail.next = temp
        # обновляем указатель конца
        # очереди на вновь добавл. нод
        self.tail = temp

    def size(self):
        return self.current_size
    
# if __name__== '__main__':
#     q = ListQueue()
#     q.put(-34)
#     q.put(-24)
#     q.get()
#     print(q.size())
#     q.get()
#     print(q.size())

#     q.get()
#     q.get()
#     q.put(80)
#     print(q.size())
#     print("Queue Front " + str(q.head.val))
#     print("Queue Rear " + str(q.tail.val))

if __name__ == "__main__":
    my_queue = ListQueue()
    cmd_num = int(input())
    for _ in range(cmd_num):
        cmd = input().split()
        if cmd[0] == 'get':
            if my_queue.size():
                val = my_queue.head.val
                my_queue.get()
                print(val)
            else:
                print('error')
        if cmd[0] == 'put':
            my_queue.put(int(cmd[1]))
        if cmd[0] == 'size':
            print(my_queue.size())

