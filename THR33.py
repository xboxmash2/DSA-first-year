arr= [12,7,8,9,12,45,67]
m=0
n=0
for i in arr:
    if i>m:
        n=m
        m=i
    elif i>n:
        n=i
print(m,n)
