#!/usr/bin/env python

n,k=map(int,input().split())
num=list(input())
stack=[]
K=k
for i in range(n):
    while k>0 and stack and stack[-1]<num[i]:
        stack.pop()
        k-=1
    stack.append(num[i])

print(''.join(stack[:n-K]))
