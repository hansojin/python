#!/usr/bin/env python

import sys
input= sys.stdin.readline

case=int(input())
for num in range(case):
    n,m=map(int,input().split())
    
    li=[]
    for _ in range(n):
        li.append(list(map(int,input().split())))
    
    maxx=-1
    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp=0
            for l in range(i,i+m):
                for k in range(j,j+m):
                    tmp+=li[l][k]
            if tmp>maxx:
                maxx=tmp
    print(f'#{num+1} {maxx}')

            
