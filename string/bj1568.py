#!/usr/bin/env python

n=int(input())
cnt,i=0,1
while n!=0:
    if n<i:
        i=1
    n-=i
    i+=1
    cnt+=1
print(cnt)
