#!/usr/bin/env python

import sys
input =sys.stdin.readline

for _ in range(int(input())):
    cnt=0
    li=[]
    for i in range(int(input())):
        li.append(list(map(int,input().split())))
    li.sort(key= lambda x : x[0])
    maxx=li[0][1]+1
    for i in range(len(li)):
        if maxx>li[i][1]:
            maxx=li[i][1]
            cnt+=1
    print(cnt)
