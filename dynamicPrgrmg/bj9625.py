#!/usr/bin/env python

a=[0,1,1]
b=[1,1,2]
for i in range(3,46):
    a.append(a[i-1]+a[i-2])
    b.append(b[i-1]+b[i-2])
n=int(input())
print(a[n-1],b[n-1])



