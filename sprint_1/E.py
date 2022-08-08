def get_longest_word(line: str) -> str:
    splitted = line.split(' ')
    max_len = len(splitted[0])
    longest = splitted[0]
    for i in range(1, len(splitted)):
        curr_len = len(splitted[i])
        if curr_len > max_len:
            max_len = curr_len
            longest = splitted[i]
    return longest

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))