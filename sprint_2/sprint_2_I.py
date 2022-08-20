# -*- coding: utf-8 -*-
# https://contest.yandex.ru/contest/22779/problems/I/


class MyQueueSized:
	"""
	Kласс MyQueueSized, который принимает параметр max_size, 
	означающий максимально допустимое количество элементов в очереди.
	"""
	def __init__(self, max_size: int) -> None:
		self.queue = [0] * max_size
		self.max_size = max_size
		self.head = 0
		self.tail = 0
		self.curr_size = 0

	def push(self, x: int) -> None:
		if self.curr_size < self.max_size:
			self.queue[self.tail] = x 
			self.tail = (self.tail + 1) % self.max_size
			self.curr_size += 1

	def pop(self) -> int:
		x = self.queue[self.head]
		self.queue[self.head] = None
		self.head = (self.head + 1) % self.max_size
		self.curr_size -= 1
		return x

	def peek(self) -> int:
		return self.queue[self.head]

	def size(self) -> int:
		return self.curr_size



if __name__ == '__main__':
	cmd_num = int(input())
	m_size = int(input())
	my_queue_sized = MyQueueSized(m_size)
	for _ in range(cmd_num):
		cmd = input().split()
		if cmd[0] == 'push':
			if my_queue_sized.size() < m_size:
				my_queue_sized.push(cmd[1])
			else:
				print('error')
		if cmd[0] == 'pop':
			if my_queue_sized.size():
				print(my_queue_sized.pop())
			else:
				print("None")
		if cmd[0] == 'peek':
			if my_queue_sized.size():
				print(my_queue_sized.peek())
			else:
				print("None")
		if cmd[0] == 'size':
			print(my_queue_sized.size())

