#!/usr/bin/env python

n=int(input())
w=input().rstrip()
cnt=0
for i in range(n//2):
    if w[i]!=w[len(w)-1-i]:
        cnt+=1
print(cnt)
