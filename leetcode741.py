# coding=utf-8

import sys


def kill_monster(matrix):
    if not matrix:
        return 0
    n = len(matrix)
    dp = [[float("-inf")]*n for _ in range(n)]
    dp[0][0] = matrix[0][0]

    for k in range(1, 2*n-1):
        dp2 = [[float("-inf")]*n for _ in range(n)]
        for i in range(max(0, k-(n-1)), min(n-1, k)+1):
            for j in range(max(0, k-(n-1)), min(n-1, k)+1):
                if matrix[i][k-i] == -1 or matrix[j][k-j] == -1:
                    continue
                val = matrix[i][k-i]
                if i != j:
                    val += matrix[j][k-j]

                for pi in [i-1, i]:
                    for pj in [j-1, j]:
                        if pi < 0 or pj <0:
                            continue
                        dp2[i][j] = max(dp2[i][j], dp[pi][pj]+val)
        dp = dp2
    return max(0, dp[n-1][n-1])


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    mat = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        a = list(map(int, line.split()))
        mat.append(a)
    print(kill_monster(mat))