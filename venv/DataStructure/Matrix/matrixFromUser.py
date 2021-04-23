#Input from User
R=int(input("Enter number of Rows "))
C=int(input("Enter number of Columns "))

#Intialize Matrix
matrix=[]

for i in range(R):
    row=[]
    for j in range(C):
        value=int(input("Enter [{}][{}] of matrix ".format(i,j)))
        row.append(value)
    matrix.append(row)

for i in  range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()




