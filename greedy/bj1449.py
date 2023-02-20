#!/usr/bin/env python

import sys
input = sys.stdin.readline

a,b=map(int,input().split())
pipe=[False]*10001
num = list(map(int, input().split()))
for i in num:
    pipe[i]=True

cnt=0

for i in range(10001):
    if pipe[i]==True:
        for j in range(i,i+b):
            pipe[j]=False
        cnt+=1
print(cnt)
