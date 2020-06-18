# coding: utf-8


def generate_matrix(n):
    """
    Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
    :param n: int
    :return: List[List[int]]
    """
    if n < 1:
        return []

    ret = [[0] * n for _ in range(n)]
    r = c = 0
    j = m = n
    while r < m and c < n:
        for i in range(c, n):
            if i == 0:
                ret[r][i] = i + 1
            else:
                ret[r][i] = ret[r][i - 1] + 1
        r += 1

        for i in range(r, m):
            if n == j:
                ret[i][n - 1] = i + n
            else:
                ret[i][n - 1] = ret[i - 1][n - 1] + 1
        n -= 1

        if r < m:
            for i in range(n - 1, c - 1, -1):
                ret[m - 1][i] = ret[m - 1][i + 1] + 1
            m -= 1

        if c < n:
            for i in range(m - 1, r - 1, -1):
                ret[i][c] = ret[i + 1][c] + 1
            c += 1

    return ret


if __name__ == "__main__":
    result = generate_matrix(1)
    for i in result:
        print(i, end='\n')




