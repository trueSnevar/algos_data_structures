# -*- coding: utf-8 -*-

def is_palindrome(line: str) -> bool:
    """ Checks is a given string
    is a palindrome.

    Consider alphanumeric symbols only.
    Big and small chars treated the same.

    - Example input: A man, a plan, a canal: Panama
    - Output: True

    """
    normalized = ''.join([char.lower() for char in line if char.isalpha()])
    reversed_str = normalized[::-1]
    return normalized == reversed_str

if __name__ == "__main__":
    print(is_palindrome(input().strip()))