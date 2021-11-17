direction = [(-1,0), (0,1), (1,0), (0,-1)]

def is_valid_cell(arr, row, col, visited):
    if (row >= 0 and row < len(arr) and
        col >= 0 and col < len(arr[0]) and
        (row, col) not in visited):
        return True
    else:
        return False    

def DFS_traversal(arr, row, col, visited = [], output = []):
    global direction
    output.append(arr[row][col])
    visited.append((row, col))
    for d in direction:
        new_row = row + d[0]
        new_col = col + d[1]
        if is_valid_cell(arr, new_row, new_col, visited):
            DFS_traversal(arr, new_row, new_col, visited, output)
    return output                    

if __name__ == "__main__":
    arr = [ [1,     2,  3,  4,  5],
            [6,     7,  8,  9,  10],
            [11,    12, 13, 14, 15],
            [16,    17, 18, 19, 20]]
    print(DFS_traversal(arr, 1, 2))        