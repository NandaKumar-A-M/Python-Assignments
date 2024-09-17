import numpy as np
def matrix_inverse(matrix):
    matrix1=np.array(matrix)
    print("Entered matrix is ",matrix1)
    try:
        inv_matrix=np.linalg.inv(matrix1)
        print("Matrix is invertible the inverted matrix is: ")
        print(inv_matrix)
    except np.linalg.Error:
        print("Matrix is not possible to invert")


rows=int(input("Enter the number of rows: " ))
cols=int(input("Enter the number of columns: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        a=int(input(f"Enter {i,j} element"))
        row.append(a)
    matrix.append(row)
print("The entered matrix is: ")
for i in matrix:
    print(i)
matrix_inverse(matrix)
