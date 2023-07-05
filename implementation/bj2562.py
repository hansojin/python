#!/usr/bin/env python

arr=[]
for i in range(9):
    arr.append(int(input()))

maxx=max(arr)
print(maxx)
print(arr.index(maxx)+1)
