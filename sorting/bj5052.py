#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    li=[]
    cnt=0
    n=int(input())
    for _ in range(n):
        num=str(input().rstrip())
        li.append([num,len(num)])
        li.sort(key=lambda x : x[1])
   
        for i in range(0,n-1):
            for j in range(i,n):
                tmp=len(li[i])
                if li[i][0]==(li[j][0])[:tmp]:
                    cnt+=1
                    break
        if cnt==1:
            print('NO')
        else:
            print('YES')
