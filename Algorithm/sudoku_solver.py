import queue
from typing import List

def solve_sudoku(board: List[List[str]]) -> List[List[str]]:

    def is_valid_num(board: List[List[str]], row: int, col: int, num: str) -> bool:
        subgrid = [board[i][j] for i in range(row // 3 * 3, row // 3 * 3 + 3) for j in range(col // 3 * 3, col // 3 * 3 + 3)]
        for i in range(len(board)):
            if board[row][i] == num or board[i][col] == num or subgrid[i] == num or num == ".":
                return False
        return True

    def backtrack() -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid_num(board, i, j, num):
                            print(i, j, num)
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = '.'
                            print("Executed BackTracking")
                    return False
        return True

    if not board or len(board) != 9 or len(board[0]) != 9:
        raise ValueError("Invalid Sudoku board")

    if backtrack():
        return board

    return False

if __name__ == "__main__":
    board = [["8", ".", ".", ".", ".", ".", "9", ".", "."],
             [".", "9", "5", "7", "2", ".", "6", ".", "."],
             ["7", "4", ".", ".", ".", "9", ".", ".", "1"],
             [".", ".", ".", ".", "9", ".", ".", ".", "."],
             ["9", "6", "1", "3", "7", "4", ".", ".", "."],
             [".", ".", ".", ".", "1", ".", ".", "6", "9"],
             ["2", "8", ".", ".", "3", "7", ".", ".", "."],
             [".", ".", ".", "2", ".", "1", "7", ".", "."],
             ["3", ".", "7", ".", ".", ".", "2", ".", "4"]]
    new_board = solve_sudoku(board)
    
    if solve_sudoku(board):
        for row in board:
            print(''.join(str(row)))
    else:
        print("No solution exists.")