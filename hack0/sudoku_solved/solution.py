def valid(digits):
    return sorted(digits) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sudoku_solved(sudoku):
    for i in range(9):
        row = sudoku[i]
        column = [p[i] for p in sudoku]
        if not valid(row) and not valid(column):
            return False
    for i in range(3):
        for j in range(3):
            box = [sudoku[x][y] for x in range(0 + i * 3, 3 + i * 3)
                    for y in range(0 + j * 3, 3 + j * 3)]
            if not valid(box):
                return False
    return True