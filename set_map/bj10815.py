#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
n_li=list(map(int,input().split()))

m=int(input())
m_li=list(map(int,input().split()))

for i in m_li:
    if i in n_li:
        
        print(1, end=' ')
    else: print(0, end=' ')
