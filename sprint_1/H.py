# -*- coding: utf-8 -*-

from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    res = ''
    carry = ''
    diff = abs(len(first_number) - len(second_number))
    if len(first_number) > len(second_number):
        second_number = second_number.zfill(diff+len(second_number))
    elif len(first_number) < len(second_number):
        first_number = first_number.zfill(diff+len(first_number))
    for i in range(len(first_number)-1, -1, -1):
        if (first_number[i] == '1' and second_number[i] == '1'):
            if not carry:
                res += '0'
                carry += '1'
            else:
                res += '1'
        elif (first_number[i] == '0' and second_number[i] == '0'):
            if not carry:
                res += '0'
            else:
                res += '1'
                carry = ''    
        else:
            if not carry:
                res += '1'
            else:
                res += '0'

    if carry:
        res += carry

    return res[::-1]

def get_sum_of_bins(first_number: str, second_number: str) -> str:
    """ Sums up two binary nums, represented as strings.

    - Example input: 1010
                     1011

    - Output: 10101
    
    """
    if len(second_number) > len(first_number):
        first_number, second_number = second_number, first_number
    diff = len(first_number) - len(second_number)
    second_number = '0' * diff + second_number

    res = ''
    carry = 0
    for i in range(len(first_number)-1, -1, -1):
        s = int(first_number[i]) + int(second_number[i]) + carry
        if s > 1:
            s -= 2
            carry =1 
        else:
            carry = 0
        res = str(s) + res
    if carry:
        res = '1' + res
    return res

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))