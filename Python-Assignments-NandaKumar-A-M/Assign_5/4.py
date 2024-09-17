def saddle_point(matrix):
    for i in range(row):
        for j in range(col):
            value=matrix[i][j]
            for k in range(col):
                if value<=matrix[i][k]:
                    min_in_row=True
                # if value>=matrix[i][k]:       # -------------for vice versa
                #     max_in_row=True            #------------
            for k in range(row):
                if value>=matrix[k][j]:
                    max_in_col=True
                # if value<=matrix[k][j]:      # ----------------for vice versa
                #     min_in_col=True          #----------------

    if (min_in_row and max_in_col)==True:
        print("Saddle point exists in this matrix")
    # elif (max_in_row and min_in_col)==True:   # ----------------for vice versa
    #     print("Saddle point exists in this matrix")    # ----------------for vice versa
    else:
        print("Saddle point not exists in this matrix")
           
            
            
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
saddle_point(matrix)