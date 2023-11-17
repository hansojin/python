#!/usr/bin/env python

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
    #return table[-1]
    return table

n=int(input())
on=sorted(list(map(int,input().split())))
tw=sorted(list(map(int,input().split())))
one = [on[i+1]-on[i] for i in range(n-1)]
two = [tw[i+1]-tw[i] for i in range(n-1)]

if kmp(one)==kmp(two):
    print('possible')
else:
    print('impossible')

