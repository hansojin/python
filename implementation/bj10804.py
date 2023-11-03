#!/usr/bin/env python

li=[x for x in range(0,21)]

for _ in range(10):
    s,e = map(int,input().split())
    cnt=(e-s+1)//2
    for i in range(cnt):
        li[s+i],li[e-i]=li[e-i],li[s+i]

for i in range(1,21):
    print(li[i],end=' ')

