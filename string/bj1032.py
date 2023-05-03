#!/usr/bin/env python

n=int(input())
li=[]
pri=[]
for _ in range(n):
    li.append(input())

for i in range(len(li[0])):
    ans=True
    for j in li:
        tmp=li[0][i]
        if tmp!=j[i]:
            ans=False
            break
    if ans==True:
        pri.append(tmp) 
    else:
        pri.append('?')

for i in pri:
    print(i,end='')

