#!/usr/bin/env python

cnt=0
n=input().rstrip()
while True:
    if len(n)==1:
        print(cnt)
        break
    sum=1
    cnt+=1
    for i in range(len(n)):
        sum*=int(n[i])
    n=str(sum)
