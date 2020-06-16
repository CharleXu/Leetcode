# coding: utf-8


def spiral_order(matrix):
    """
    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
    :param matrix: List[List[int]]
    :return: List[int]
    """
    if not matrix:
        return []

    ret = []
    m, n = len(matrix), len(matrix[0])
    i = j = k = 0
    while j < m and k < n:
        for i in range(k, n):
            ret.append(matrix[j][i])
        j += 1

        for i in range(j, m):
            ret.append(matrix[i][n - 1])
        n -= 1

        if j < m:
            for i in range(n - 1, k - 1, -1):
                ret.append(matrix[m - 1][i])
            m -= 1

        if k < n:
            for i in range(m - 1, j - 1, -1):
                ret.append(matrix[i][k])
            k += 1

    return ret


if __name__ == "__main__":
    li = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(spiral_order(li))
