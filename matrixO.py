rows=int(input("enter rows"))
cols=int(input("enter columns"))
matrix=[]
for i in range(rows):
    arr=[]
    for j in range(cols):
        arr.append(int(input("enter value")))
    matrix.append(arr)
print("OG=",matrix)
#rotate by 90*
    #first transpose
# for i in range(rows):
#     for j in range(i,cols):
#         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

trows=cols
tcols=rows

transpose=[]

for r in range(trows):
    arr=[]
    for c in range(tcols):
        arr.append(matrix[c][r])
    transpose.append(arr)
    
print("TRANSPOSE")
print(transpose)
    # then REVERSE OF EACH ROW

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    #DO NOT USE WITH OTHER CODE
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

# for r in range(trows):
#     transpose[r].reverse()
# print("AFTER ROTATION BY 90*")
# print(transpose)


# ANTI CLOCKWISE ROTATION

transpose.reverse()

print(" AFTER ANTI CLOCKWISE ROTATION")
print(transpose)