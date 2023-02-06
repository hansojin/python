#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
n_li=list(map(int,input().split()))
sset=set(n_li)
m=int(input())
m_li=list(map(int,input().split()))

for i in m_li:
    if i in sset:
        print(n_li.count(i), end=' ')
    else: print(0, end=' ')

