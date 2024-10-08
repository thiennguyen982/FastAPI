import sudoku_backtracking

board = [["6", "5", "4", "3", "9", "7", "8", "2", "1"],
            ["8", "2", "3", "1", "6", "4", "9", "7", "5"],
            ["1", ".", ".", "2", "5", "8", "3", "6", "4"],
            ["2", ".", "6", "5", "7", ".", ".", ".", "."],
            [".", ".", ".", ".", "1", "6", "5", ".", "."],
            [".", "1", ".", ".", ".", ".", ".", "3", "."],
            [".", ".", ".", "7", ".", ".", "6", ".", "."],
            ["3", ".", "1", ".", ".", "9", ".", "5", "."],
            ["4", "6", ".", ".", ".", ".", "2", "9", "."]]
new_board = sudoku_backtracking.solution(board)
print(new_board)