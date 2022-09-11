# coding: utf-8
# Successful submition: 70312603

"""
ПРИНЦИП РАБОТЫ
    Реализация простой hash-таблицы выполнена с использованием двух массивов,
    один из которых хранит ключи, а второй - значения элементов hash-таблицы.
    Коллизии разрешаются методом открытой адресации с линейным пробированием    
ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    Если два значения хэшируются на один ключ, то нужно каким-то образом
    разместить в хэш-таблице второй элемент.
    В качестве такого метода выбран поиск другой свободной корзины для размещения в ней
    данного значения.
    Проще всего в этом случае начать с оригинальной корзины хэша и просматривать далее по одной, пока не будет найдена свободная корзина
    Такой процесс и называется методом открытой адресации, поскольку пытается найти следующее свободное место в хэш-таблице.
ВРЕМЕННАЯ СЛОЖНОСТЬ
    Для поиска необходимого значения используется хэш-функция, то есть на вход
    получается ключ, далее для ключа вычисляется хэш, хэш сопоставляется со значением
    в списке значений.
    И вычисление хэша, и поиск в массиве по индексу занимет O(1) константное время.

    Однако, если в построенной хэш-таблице много коллизий, то в худшем случае может потребоваться O(n) времени для нахождения нужного значения, так как придется постоянно переходить к следующей корзине, пока таблица не будет пройдена целиком.
    Именно поэтому важно применять хорошую хэш-функцию.
ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Для хранения n значений требуется O(n) памяти.
"""


class MyHashTable:
    def __init__(self):
        self.__capacity = 10**7
        self._keys = [None] * self.__capacity
        self._values = [None] * self.__capacity 

    @property
    def capacity(self):
        return self.__capacity
    
    def _resolve_collision(self, prev_hash):
        return (prev_hash + 1) % self.capacity
    
    def _find_value(self, hashed, key):
        while self._keys[hashed] and self._keys[hashed] != key:
            hashed = self._resolve_collision(hashed)
        return hashed
    
    def put(self, key, value):
        hashed_key = key % self.capacity
        if not self._keys[hashed_key]:
            self._keys[hashed_key] = key
            self._values[hashed_key] = value
        elif self._keys[hashed_key] == key:
            self._values[hashed_key] = value
        else:
            new_hashed_key = self._find_value(hashed_key, key)
            if self._keys[new_hashed_key] is None:
                self._keys[new_hashed_key] = key
                self._values[new_hashed_key] = value
            else:
                self._values[new_hashed_key] = value      

    def get(self, key):
        hashed_key = key % self.capacity
        new_key = self._find_value(hashed_key, key)
        if self._keys[new_key] == key:
            return self._values[new_key]
        return None

    def delete(self, key):
        value = self.get(key)
        if value:
            self.put(key, None)
        return value


if __name__ == "__main__":
    my_hash_table = MyHashTable()
    n = int(input())
    for _ in range(n):
        cmd = input().split()
        if len(cmd) == 2:
            print(getattr(my_hash_table, cmd[0])(int(cmd[1])))
        else:
            getattr(my_hash_table, cmd[0])(*map(int, cmd[1:]))

