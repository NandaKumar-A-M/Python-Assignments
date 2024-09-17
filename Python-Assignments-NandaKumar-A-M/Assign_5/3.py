def rotate90D(matrix):
    if len(matrix)==0:
        print("Matrix has 0 values")
    else:
        rotated_matrix= [ [0]*row for i in range(col)]
        for i in range(row):
            for j in range(col):
                rotated_matrix[j][row-1-i]=matrix[i][j]

    print("90 Degree Rotated matrix is : ")
    for i in rotated_matrix:
        print(i)


row=int(input("Enter the number of rows"))
col=int(input("Enter the number of columns"))
matrix=[]
for i in range(row):
    rows=[]
    for j in range(col):
        a=int(input(f"Enter the [{i+1},{j+1}] element"))
        rows.append(a)
    matrix.append(rows)
print("Given input matrix is")
for rows in matrix:
    print(rows)
rotate90D(matrix)

