def spiral(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1
        if top <= bottom:
            for i in range(top, bottom + 1):
                print(matrix[i][right], end=" ")
        right -= 1
        if left <= right and top <= bottom:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1
        if top <= bottom and left <= right:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1

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

print("Spiral order traversal:")
spiral(matrix)
