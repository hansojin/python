#!/usr/bin/env python

n=int(input())

def hanoi(n, start, end, sub):
    if n==1:
        print(start, end)
        return
    else:
        hanoi(n-1,start,sub,end)
        print(start, end)
        hanoi(n-1,sub,end,start)

hanoi(n,1,3,2)
