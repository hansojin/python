#!/usr/bin/env python

mylist= [list(map(int,input().split())) for _ in range(9)]

max_value=max(map(max,mylist))
print(max_value)

for i in range(9):
    for j in range(9):
        if mylist[i][j]==max_value:
            print(i+1,j+1,end=' ')
