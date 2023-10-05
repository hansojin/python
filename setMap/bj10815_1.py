#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
li.sort()

def bin_search(num):
    l=0
    r=n-1
    while l<=r:
        mid=(l+r)//2
        
        if li[mid]==num:
            return 1
        elif li[mid]>num:
            r=mid-1     #범위 반으로 줄이기
        else:
            l=mid+1
    return 0

int(input())
for num in list(map(int,input().split())):
    print(bin_search(num), end=' ')
