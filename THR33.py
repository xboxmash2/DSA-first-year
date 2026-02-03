# FIRST MAXIMUM AND SECOND MAXIMUM
import math
arr= [12,7,8,9,12,45,67]
m=-math.inf
n=-math.inf
for i in arr:
    if i>m:
        n=m
        m=i
    elif i>n:
        n=i
print(m,n)
