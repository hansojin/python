#/usr/bin/env python

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    print((max(li)-min(li))*2)
