rows=int(input("enter rows"))
cols=int(input("enter columns"))
matrix=[]
for i in range(rows):
    arr=[]
    for j in range(cols):
        arr.append(int(input("enter value")))
    matrix.append(arr)
print(matrix)

# #UPPER triangle

# for r in range(rows-1):
#     for c in range(r+1,cols):
#         print(matrix[r][c],end=" ")

# print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

# #LOWER triangle

# for r in range(1,rows):
#     for c in range(r):
#         print(matrix[r][c],end=" ")

#TRANSPOSE

# matrics=[]
# for i in range(rows):
#     arr=[]
#     for j in range(cols):
#         arr.append(matrix[j][i])
#     matrics.append(arr)
# print("TRANSPOSE")
# print(matrics)

for i in range(rows):
    for j in range(i,cols):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
print(matrix)
