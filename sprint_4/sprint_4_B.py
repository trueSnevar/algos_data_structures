# coding: utf-8

from dataclasses import dataclass
import datetime
from time import sleep

class AggrKey:
    def __init__(self, begin_time, truck_id, shovel_id, unload_id, work_type_id, load_type_id):
        self.interval_begin = begin_time
        self.truck_id = truck_id
        self.shovel_id = shovel_id
        self.unload_id = unload_id
        self.work_type_id = work_type_id
        self.load_type_id = load_type_id

    def __key(self):
        return self.interval_begin, self.truck_id, self.shovel_id, self.unload_id, self.work_type_id, self.load_type_id

    def __eq__(self, other) -> bool:
        return self.key == other.key

    def __gt__(self, other):
        for s, o in zip(self.key, other.key):
            if s == o:
                continue
            if s is None:
                return False
            if o is None:
                return True
       #return hash(self.key) > hash(other.key)
                    

    def __lt__(self, other):
        return hash(self.key) < hash(other.key)

    def __hash__(self) -> int:
        return hash(self.__key())

    @property
    def key(self):
        return self.__key()

def main():
    now = datetime.datetime.now()
    key_1 = AggrKey(now, 1, 2, 3, 4, 5)
    now1 = datetime.datetime.now()
    key_2 = AggrKey(now, 1, 2, 3, None, 5)
    print(key_1 == key_2)
    print(key_1 > key_2) 
    print(key_1 < key_2)

if __name__ == "__main__":
    main()