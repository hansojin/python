#!/usr/bin/env python

import sys
input=sys.stdin.readline

a,b=map(int,input().split())
li=list(map(int,input().split()))

tot=[]
maxx=0
for i in range(a-2):
    for j in range(i+1,a-1):
        for l in range(j+1,a):
            if li[i]+li[j]+li[l] > b : 
                continue
            else:
                res= li[i]+li[j]+li[l]
                if maxx<= res:
                    maxx=res

print(maxx)
            


