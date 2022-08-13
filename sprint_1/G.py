# -*- coding: utf-8 -*-

def dec_to_binary(n: int) -> str:
    """ Converts input decimal non negative 
    integer into binary.

    - Example input: 13
    - Output: '1101'

    """
    res = ''
    while n > 0:
        bit = str(n % 2)
        res = bit + res
        n //= 2
    return res

if __name__ == "__main__":
    n = int(input())
    print(dec_to_binary(n))