# coding: utf-8

def reverse_string(s: str) -> str:
    lst = list(s.split())
    lst.reverse()
    return ' '.join(lst)

if __name__ == "__main__":
    st = input()
    print(reverse_string(st))