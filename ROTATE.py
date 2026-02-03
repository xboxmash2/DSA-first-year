import array
a=[1,3,5,7,9,11]

k=int(input("enter no."))
for i in range(k):
    last=a[-1]
    for j in range(len(a)-1,0,-1):
        a[j]=a[j-1]
    a[0]=last

print(a)
