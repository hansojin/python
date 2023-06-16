#!/usr/bin/env python

n=int(input())
li=list(map(int,input().split()))

li.sort(reverse=True)
sum=0
score,tot=0,0

for i in range(n-1):
    score=li[i]*li[i+1]
    li[i+1]=li[i]+li[i+1]
    tot=tot+score
print(tot)
