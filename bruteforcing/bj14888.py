#!/usr/bin/env python

import sys
input =sys.stdin.readline
from itertools import permutations

n= int(input())
num=list(map(int,input().split()))
op_num=list(map(int,input().split()))
op_list=['+', '-', '*', '/']
op=[]

for i in range(4):
    for j in range(op_num[i]):
        op.append(op_list[i])
maxx=-1e9
minn=1e9

for i in permutations(op,n-1):
    total=num[0]
    for j in range(1,n):
        if i[j-1]=='+':
            total+=num[j]
        elif i[j-1]=='-':
            total-=num[j]
        elif i[j-1]=='*':
            total*=num[j]
        elif i[j-1]=='/':
            total=int(total/num[j])
    if total>maxx:
        maxx=total
    if total<minn:
        minn=total
print(maxx)
print(minn)



