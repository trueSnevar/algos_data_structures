# coding: utf-8
# https://leetcode.com/problems/unique-binary-search-trees/discuss/31826/Python-solutions-(DP-%2B-Catalan-number)


def num_trees(n: int) -> int:
    res = [1] * (n+1)

    for nodes in range(2, n+1):
        total = 0
        for root in range(1, nodes+1):
            left = root - 1
            right = nodes - root
            total += res[left] * res[right]
        res[nodes] = total
    return res[n]

if __name__ == "__main__":
    n = int(input())
    print(num_trees(n))