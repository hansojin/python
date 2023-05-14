#!/usr/bin/env python

li=[]
for _ in range(9):
    li.append(int(input()))
total=sum(li)
two=total-100
for i in range(8):
    for j in range(i+1,9):
        if li[i]+li[j]==two:
            x,y=i,j 
            break
li.pop(x)
li.pop(y-1)
for i in li:
    print(i)
