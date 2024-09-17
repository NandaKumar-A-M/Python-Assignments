def matrix_Mul(matrix1,matrix2):
    if len(matrix1[0])!=(len(matrix2)):
        print("Matrix multiplication is not possible")
    else:
        mul_matrix=[[0 for i in range(len(matrix2[0]))] for i in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    mul_matrix[i][j]+=matrix1[i][k]*matrix2[k][j]
        print("The multiplied matrix is: ")
        for i in mul_matrix:
            print(i)
        
row1=int(input("Entre the number of rows in MATRIX 1 : "))
col1=int(input("Entre the number of cols in MATRIX 1 : "))
row2=int(input("Enter the numner os rows in MATRIX 2 : "))
col2=int(input("Enter the number of cols in MATRIX 2 : "))

matrix1=[]
matrix2=[]
print("Enter input for MATRIX 1")
for i in range(row1):
    rows=[]
    for j in range(col1):
        a=int(input(f"Enter the [{i+1},{j+1}] element"))
        rows.append(a)
    matrix1.append(rows)
    
print("Enter input for MATRIX 2")
for i in range(row2):
    rows=[]
    for j in range(col2):
        a=int(input(f"Enter the [{i+1},{j+1}] element"))
        rows.append(a)
    matrix2.append(rows)

print("Given input matrix 1 is :")
for rows in matrix1:
    print(rows)
print("Given input matrix 2 is :")
for rows in matrix2:
    print(rows)
matrix_Mul(matrix1,matrix2)
