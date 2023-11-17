#!/usr/bin/env python

import sys
input= sys.stdin.readline

def kmp(pattern):
    plen=len(pattern)
    table=[0 for _ in range(plen)]
    i=0
    for j in range(1,plen):
        while i>0 and pattern[i]!=pattern[j]:
            i=table[i-1]
        if pattern[i]==pattern[j]:
            i+=1
            table[j]=i
    return table[-1]

while True:
    pattern = input().rstrip()
    if pattern=='.':
        break
    plen = len(pattern)
    res = kmp(pattern)
    if plen%(plen-res)!=0:
        print(1)
    else:
        print(plen//(plen-res))
