#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,k=map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

li.sort(key=lambda x : (-x[1],-x[2],-x[3]))

for i in range(n):
    if li[i][0]==k:
        idx=i
for i in range(n):
    if li[idx][1:]==li[i][1:]:
        print(i+1)
        break
