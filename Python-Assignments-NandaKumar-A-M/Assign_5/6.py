def search_sorted_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1 
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return row+1, col+1 
        elif matrix[row][col] > target:
            col -= 1  
        else:
            row += 1  
    return -1, -1  

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
matrix = []

for i in range(row):
    rows = []
    for j in range(col):
        a = int(input(f"Enter the element at position [{i+1}, {j+1}]: "))
        rows.append(a)
    matrix.append(rows)

print("Given input matrix is:")
for rows in matrix:
    print(rows)
target=int(input("Enter the target"))
result = search_sorted_matrix(matrix, target)
print("Found at position",result) 
