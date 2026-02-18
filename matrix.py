rows=int(input("enter rows"))
cols=int(input("enter columns"))
matrix=[]
for i in range(rows):
    arr=[]
    for j in range(cols):
        arr.append(int(input("enter value")))
    matrix.append(arr)
print(matrix)


# for i in matrix:
#     for j in i:
#         print(j)

colindex=int(input("enter column index"))
rowindex=int(input("enter row index"))

print(matrix[rowindex][colindex])

for i in range(len(matrix[0])): #diagonal left to right PRIMARY
    print(matrix[i][i],end="")

print("\n")

for i in range(len(matrix[0])): #diagonal right to left SECONDARY
    print(matrix[i][-i-1],end="")

print("\n")

for i in matrix:
    print("ROW SUM =",sum(i))

#diagonal SUM PRIMARY
sum=0
for i in range(rows):
    sum+=matrix[i][i]
print("PRIMARY SUM =",sum)

#diagonal SUM SECONDARY
sum=0
for i in range(rows):
    sum+=matrix[i][cols-1-i]
print("SECONDARY SUM =",sum)



