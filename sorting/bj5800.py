#!/usr/bin/env python

n=int(input())
for j in range(1,n+1):
    li=list(map(int,input().split()))
    del li[0]
    li.sort()
    print(f'Class {j}')
    tmp=[]
    for i in range(len(li)-1):
        tmp.append(li[i+1]-li[i])
    print(f'Max {li[-1]}, Min {li[0]}, Largest gap {max(tmp)}')


