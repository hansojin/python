#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[]

for _ in range(n):
    li.append(input().rstrip())

a,b=0,0
for i in range(n):
    if 'X' not in li[i]:
        a+=1

for j in range(m):
    if 'X' not in [li[i][j] for i in range(n)]:
        b+=1
print(max(a,b))
    
