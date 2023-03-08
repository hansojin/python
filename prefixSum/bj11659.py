#!/usr/bin/env python

import sys
input = sys.stdin.readline


a,b=map(int,input().split())
li=list(map(int,input().split()))

prefix_sum=[0]
tmp=0
for i in li:    #미리 계산합을 구해서 배열에 저장
    tmp+=i
    prefix_sum.append(tmp)

for i in range(b):
    m,n=map(int,input().split())
    print(prefix_sum[n]-prefix_sum[m-1])

