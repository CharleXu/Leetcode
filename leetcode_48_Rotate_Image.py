# coding: utf-8


# def rotate(matrix):
#     """
#     Rotate the matrix in place by 90 degrees (clockwise)
#     :param matrix: List[List[int]]
#     :return: None
#     """
#     if not matrix:
#         return
#
#     n = len(matrix)
#     step = n
#     if step % 2 != 0:
#         step += 1
#
#     for i in range(n // 2):
#         for j in range(step // 2):
#             matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], \
#             matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j], \
#                                    matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]

def rotate(matrix):
    """
    Rotate the matrix in place by 90 degrees (clockwise)
    :param matrix: List[List[int]]
    :return: None
    """
    matrix[:] = zip(*matrix[::-1])


if __name__ == "__main__":
    image = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    rotate(image)
    print(image)
