#!/usr/bin/env python

a=int(input())
b=int(input())
c=int(input())
n=a*b*c
arr=[0]*10
n=list(map(int,str(n)))
for i in n:
    arr[i]+=1
for i in arr:
    print(i)
