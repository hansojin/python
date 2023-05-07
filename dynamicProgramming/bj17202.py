#!/usr/bin/env python

a=input()
b=input()
li=[]
for i in range(len(a)):
    li.append(a[i])
    li.append(b[i])

while len(li)!=2:
    tmp=[]
    for i in range(len(li)-1):
        num=int(li[i])+int(li[i+1])
        tmp.append(int(num)%10)
    li=tmp
print(*li,sep='')
