# coding: utf-8


def is_valid_sudoku(board):
    """

    :param board: List[List[str]]
    :return: bool
    """

    def is_unique(array):
        array = list(filter(lambda x: x != '.', array))
        return len(array) == len(set(array))

    for i in range(9):
        row = board[i]
        if not is_unique(row):
            return False
        col = [row[i] for row in board]
        if not is_unique(col):
            return False

    for (x, y) in [(i, j) for i in [0, 1, 2] for j in [0, 1, 2]]:
        grid = [row[3 * y: 3 * y + 3] for row in board[3 * x: 3 * x + 3]]
        if not is_unique(grid[0]+grid[1]+grid[2]):
            return False

    return True


if __name__ == "__main__":
    b = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(is_valid_sudoku(b))
