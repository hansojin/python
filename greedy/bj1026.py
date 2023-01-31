#!/usr/bin/env python

n=int(input())

numA=list(map(int,input().split()))
numB=list(map(int,input().split()))

sortA=sorted(numA)
sortB=sorted(numB,reverse=True)
a=0
for i in range(n):
    a+=sortA[i]*sortB[i]
print(a)

