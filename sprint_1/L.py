from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    """ Get an excessive letter among 
    the two given strings.

    - Example input: abcd
                     abcde

    - Output: e

    """
    shorter_count = 0
    longer_count = 0
    for char in shorter:
        shorter_count += ord(char)
    for ch in longer:
        longer_count += ord(ch)
    return chr(longer_count-shorter_count)

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))