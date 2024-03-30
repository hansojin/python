#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    A,B=[0]*5,[0]*5
    for i in a[1:]:
        A[i]+=1
    for i in b[1:]:
        B[i]+=1
    flag=False
    for i in range(4,0,-1):
        if A[i]>B[i]:
            print("A")
            flag=True
            break
        elif A[i]<B[i]:
            print("B")
            flag=True
            break
    if not flag:
        print("D")

        
