#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))

dic = dict()

for i in li:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

dic= list(zip(dic.keys(),dic.values()))

dic=sorted(dic,key= lambda x : (-x[1],x[0]))

for x,y in dic:
    for _ in range(y):
        print(x,end=' ')
