import math

def pending_one_to_nine(check_list):
    return [x for x in range(1,10) if x not in check_list]

def col_list(col, matrix):
    return [matrix[row][col] for row in range(9)]

def box_list(row, col, matrix):
    box_list = []
    start_row = 3*math.floor(row/3)
    start_col = 3*math.floor(col/3)
    for i in range(start_row, start_row+3):
        for j in range(start_col, start_col+3):
            box_list.append(matrix[i][j])
    return box_list

def intersection(row, col, matrix):
    row_pending = pending_one_to_nine(matrix[row])
    col_pending = pending_one_to_nine(col_list(col,matrix))
    box_pending = pending_one_to_nine(box_list(row,col,matrix))
    return list(set(row_pending).intersection(col_pending, box_pending))

def count_zero(matrix):
    count = 0
    for row in matrix:
        count += row.count(0)
    return count
    
def main(matrix):
    zero_count = 0
    for x in matrix:
        zero_count += x.count(0)
    while zero_count > 0:
        for row in range(9):
            for col in range(9):
                if matrix[row][col] == 0 and len(intersection(row, col, matrix)) == 1:
                    matrix[row][col] = intersection(row, col, matrix)[0]
                    zero_count -=1
    return matrix