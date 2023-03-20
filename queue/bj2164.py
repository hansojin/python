#!/usr/bin/env python

n=int(input())
cnt=n-1

q=[0]*1000000
for i in range(1,n+1):
    q[i-1]=i
ptr=0
while True:
    ptr+=1
    q[ptr+cnt]=q[ptr]
    cnt-=1
    if cnt==1:
        print(q[ptr])
        break
    ptr+=1

