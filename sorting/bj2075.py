#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
li=[]
for i in range(n):
    if i==(n-1):
        num=list(map(int,input().split()))
        for i in num:
            li.append(i)
    else:    
        num=list(map(int,input().split()))
        num.sort(reverse=True)
        li.append(num[0])
li.sort(reverse=True)   
print(li[n-1])
    

