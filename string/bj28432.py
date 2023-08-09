#!/usr/bin/env python

import sys
input= sys.stdin.readline
li=[]
comp=[]
m=int(input())
for _ in range(m):
    li.append(str(input()).strip())
n=int(input())
for _ in range(n):
    word=str(input().strip())
    if word not in li:
        comp.append(word)
if m==n==1:
    print(comp[0])
else:
    idx=li.index('?')

    if idx==0:
        e=li[idx+1][0]
        for i in comp:
            if i[-1]==e:
                print(i)
    elif idx==len(li)-1:
        s=li[idx-1][-1]
        for i in comp:
            if i[0]==s:
                print(i)

    else:
        s=li[idx-1][-1]
        e=li[idx+1][0]
        for i in comp:
            if i[0]==s and i[-1]==e:
                print(i)

