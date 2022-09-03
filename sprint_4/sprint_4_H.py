# coding: utf-8

def strange_compare(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        return "NO"
    m = {}
    m2 = {}
    for i in range(len(s1)):
        if s1[i] not in m:
            if s2[i] in m2:
                return "NO"
            m[s1[i]] = s2[i]
            m2[s2[i]] = s1[i]
        else:
            if m[s1[i]] != s2[i]:
                return "NO"
    return "YES"

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(strange_compare(s,t))