# -*- coding: utf-8 -*-

from typing import List

def get_sum_from_listed_form(l_form: str, n: int) -> List[str]:
    """ Gets the listed form of the 
    sum of two nubmers.

    - Example input: 2
                     9 5
                     17

    - Output: 1 1 2

    """
    to_num = int(l_form)
    s = to_num + n
    return [char for char in str(s)]

if __name__ == "__main__":
    n = int(input())
    l_form = ''.join(input().strip().split(' '))
    num = int(input())
    print(*get_sum_from_listed_form(l_form, num))