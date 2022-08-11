# -*- coding: utf-8 -*-

def rotate(matrix, rows, cols):
    result = []
    for i in range(cols):
        result.append([])
        for j in range(rows):
            result[i].append(matrix[j][i])
    return result

if __name__ == "__main__":
    rows = int(input())
    cols = int(input())
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().strip().split())))
    res = rotate(matrix, rows, cols)
    for i in res:
        print(*i)
