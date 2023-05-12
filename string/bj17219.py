#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,m=map(int,input().split())
#li=[]
li={}
for _ in range(n):
    a,b=map(str,input().split())
    #li.append((a,b))
    li[a]=b
#dic=dict(li)

for _ in range(m):
    #print(dic[input().rstrip()])
    print(li[input().rstrip()])
    
