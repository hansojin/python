#!/usr/bin/env python

def rev(n):
    n=list(map(str,str(n)))
    num=n[::-1]
    tmp=''.join(num)
    return int(tmp)
a,b=map(int,input().split())
print(rev(rev(a)+rev(b)))
