#!/usr/bin/env python

import sys
input = sys.stdin.readline


n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
li=list(map(int,input().split()))

def binary(num):
    left=0
    right=n-1
    mid=(left+right)//2
     
    while(left<=right):
        if num>a[mid]:
            left=mid+1
        elif num<a[mid]:
            right=mid-1
        else:
            return 1
        mid=(left+right)//2    
    
    return 0

for i in li:
    print(binary(i))

