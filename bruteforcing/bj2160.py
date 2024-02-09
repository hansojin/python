#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=[]
for i in range(n):
    li.append(list([input().rstrip() for _ in range(5)]))

a=[]
for i in range(n-1):
    for j in range(i+1,n):
        tmp=0
        for k in range(5):
            for l in range(7):
                if li[i][k][l]!=li[j][k][l]:
                    tmp+=1
        a.append((tmp,i+1,j+1))

res=min(a)
print(res[1],res[2])
