rows=int(input("enter rows"))
cols=int(input("enter columns"))
matrix=[]
for i in range(rows):
    arr=[]
    for j in range(cols):
        arr.append(int(input("enter value")))
    matrix.append(arr)
print(matrix)
#upper triangle

for r in range(rows-1):
    for c in range(r+1,cols):
        print(matrix[r][c])

