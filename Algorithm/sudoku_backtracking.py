import queue
from typing import List

def solution(board: List[List[str]]) -> List[List[str]]:
    
    def solved_board(board: List[List[str]]) -> (bool, int):
        result = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    result += 1
        if result > 0:
            return (False, result)
        return (False, result)

    def is_valid_num(board: List[List[str]], row: int, col: int, num: str) -> bool:
        subgrid = [board[i][j] for i in range(row // 3 * 3, row // 3 * 3 + 3) for j in range(col // 3 * 3, col // 3 * 3 + 3)]
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or subgrid[i] == num or num == ".":
                return False
        return True

    def solve() -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in map(str, range(1, 10)):
                        if is_valid_num(board, i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = "."
                    return False
        return True

    if solve():
        return board

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
    new_board = solution(board)
    print(new_board)
