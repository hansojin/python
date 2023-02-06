#!/usr/bin/env python

a,b=map(int,input().split())

li=[]
for _ in range(a):
    strr=str(input())
    li.append(strr)
    
cnt=0
for _ in range(b):
    word=str(input())
    if word in li:
        cnt+=1

print(cnt)
