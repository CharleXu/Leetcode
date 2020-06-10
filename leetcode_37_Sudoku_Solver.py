# coding: utf-8


def slove_sudoku(board):
    """
    Solve the Sudoku
    :param board: List[List[str]]
    :return: None
    """
    is_valid(0, 0, board)


def is_valid(row, col, board):
    if col == len(board[row]):
        col = 0
        row += 1

        if row == len(board):
            return True

    if board[row][col] != '.':
        return is_valid(row, col+1, board)

    for i in range(1, len(board)+1):
        if is_valid_sudoku(board, row, col, str(i)):
            board[row][col] = str(i)
            if is_valid(row, col+1, board):
                return True
            board[row][col] = '.'

    return False


def is_valid_sudoku(board, row, col, choice):
    """

    :param board: List[List[str]]
    :return: bool
    """
    for r in board:
        if choice == r[col]:
            return False

    for c in range(9):
        if choice == board[row][c]:
            return False

    vertical_grid = row // 3
    horizontal_grid = col // 3

    top_left_row = 3 * vertical_grid
    top_left_col = 3 * horizontal_grid

    for i in range(3):
        for j in range(3):
            if choice == board[top_left_row+i][top_left_col+j]:
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
    slove_sudoku(b)
    for i in b:
        print(i, end='\n')