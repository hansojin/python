#!/usr/bin/env python

n,k=map(int,input().split())
tmp=0
s=[1]*(n+1)

for i in range(2,n+1):
    for j in range(i,n+1):
        for j in range(i,n+1,i):
            if s[j]!=0:
                s[j]=0
                tmp+=1
                if tmp==k:
                    print(j)

            
