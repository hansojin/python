#!/usr/bin/env python

n=int(input())
num=[0]*16
num[1]=3
for i in range(2,16):
    num[i]=2*num[i-1]-1
print(num[n]**2)
