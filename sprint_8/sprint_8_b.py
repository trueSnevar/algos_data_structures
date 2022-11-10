# coding: utf-8
# https://leetcode.com/problems/one-edit-distance/description/

def is_one_edit_distance(s: str, t: str) -> bool:
    ns, nt = len(s), len(t)

    if ns > nt:
        return is_one_edit_distance(t, s)
    
    if nt - ns > 1:
        return False

    for i in range(ns):
        if s[i] != t[i]:
            if ns == nt:
                return s[i+1:] == t[i+1:]
            else:
                return s[i:] == t[i+1:]

    return ns == nt

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    res = is_one_edit_distance(s1, s2)
    print("OK" if res else "FAIL")