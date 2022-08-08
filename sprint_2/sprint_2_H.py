# -*- coding: utf-8 -*-


def is_correct_bracket_seq(brackets: str) -> bool:
    m = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    st = []
    for b in brackets:
        if b in ')}]':
            if not st or m[b] != st.pop():
                return False
        else:
            st.append(b)
    return len(st) == 0



if __name__ == '__main__':
    brackets = input()
    print(is_correct_bracket_seq(brackets))