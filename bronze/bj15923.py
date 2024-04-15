#!/usr/bin/env python

def son(a,b,c,d):
    return ((a-c)**2+(b-d)**2)**0.5

li=[]
n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    li.append((x,y))

sum=0
for i in range(n-1):
    sum+=son(li[i][0],li[i][1],li[i+1][0],li[i+1][1])

sum+=son(li[0][0],li[0][1],li[n-1][0],li[n-1][1])
print(int(sum))
