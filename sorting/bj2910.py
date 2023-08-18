#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))

dic = dict()
idx=1

for i in li:
    if i in dic:
        dic[i][0]+=1
    else:
        dic[i]=[1,idx]
        idx+=1

dic= list(zip(dic.keys(),dic.values()))

dic=sorted(dic,key= lambda x : (-x[1][0],x[1][0]))

res=[]
for i,j in dic:
    res+=[i]*j[0]
print(*res)
