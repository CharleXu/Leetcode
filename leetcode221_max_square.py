# coding: utf-8

import sys


def max_square(matrix):
    """

    :param matrix:
    :return: max_size
    """
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    for r in range(m):
        dp[r][0] = int(matrix[r][0])
    for c in range(n):
        dp[0][c] = int(matrix[0][c])
    for i in range(1, m):
        for j in range(1, n):
            if int(matrix[i][j]) == 1:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    return max(map(max, dp)) ** 2


if __name__ == "__main__":
    mat = []
    for line in sys.stdin:
        a = line.split()
        if a:
            row = []
            for num in a[0]:
                row.append(num)
            mat.append(row)
            # print(row)
        else:
            break
    print(max_square(mat))

