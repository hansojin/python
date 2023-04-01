#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=input()
li=list(map(int,input().split()))
#lis=list(set(li))
#lis.sort()
lis=sorted(list(set(li)))

dic = {lis[i] : i for i in range(len(lis))}


for i in li:
    print(dic[i],end=' ')
