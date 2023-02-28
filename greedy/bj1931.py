#!/usr/bin/env python

n=int(input())
li=[]
for _ in range(n):
    srt,end = map(int,input().split())
    li.append([srt,end])

li=sorted(li,key=lambda a:a[0])
li=sorted(li,key=lambda a:a[1])

last=0
cnt=0

for i,j in li:
    if i>=last:
        cnt+=1
        last=j
print(cnt)
