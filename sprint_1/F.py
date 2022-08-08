def is_palindrome(line: str) -> bool:
    normalized = ''.join([char.lower() for char in line if char.isalpha()])
    reversed_str = normalized[::-1]
    return normalized == reversed_str

print(is_palindrome(input().strip()))