#!/usr/bin/env python

import sys
input= sys.stdin.readline


def find(start,end):
    while start<=end:
        tmp=0
        mid =(start+end)//2
        for i in li:
            if i>mid:
                tmp+=mid
            else:
                tmp+=i
        if tmp<=m:
            start=mid+1
        else:
            end=mid-1
    return end


n=int(input())
li=list(map(int,input().split()))
m=int(input())
print(find(0,max(li)))
