# coding: utf-8
# doesn't work


def substring(s: str) -> int:
    m = {}
    best = 0
    curr = 0

    for char in s:
        if char not in m:
            curr += 1
            m[char] = True
        else:
            best = max(best, curr)
            curr = 0
    return best

if __name__ == "__main__":
    s = input().strip()
    print(substring(s))