#!/usr/bin/env python

li=[]
n=int(input())
for _ in range(n):
    li.append(input())
sn=len(li[0])
for i in range(1,sn+1):
    s=set()
    for stu in li:
        s.add(stu[-i:])
    if len(s)==n:
        print(i)
        break

    
