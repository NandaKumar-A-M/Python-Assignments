def transpose(row,col):
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

    transpose_matrix=[]
    for i in range(col):
        transpose_rows=[]
        for j in range(row):
            transpose_rows.append(matrix[j][i])
        transpose_matrix.append(transpose_rows)
    print("Transposed matrix is: ")
    for i in transpose_matrix:
        print(i)

row=int(input("Enter the number of rows"))
col=int(input("Enter the number of columns"))
transpose(row,col)