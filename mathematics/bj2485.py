#!/usr/bin/env python

import sys
input =sys.stdin.readline

def gcd_f(a,b):
    while b!=0:
        a,b=b,b%a
    return a

n=int(input())

tree=[int(input()) for _ in range(n)]
gap=[]

for i in range(1,n):
    gap.append(tree[i]-tree[i-1])

gap_set=list(set(gap))
gcd=gap_set[0]

for i in range(1,len(gap_set)):
    gcd=gcd_f(gcd,gap_set[i])

cnt=0
for gaps in gap:
    cnt+=gaps//gcd -1
print(cnt)
