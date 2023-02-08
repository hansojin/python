#!/usr/bin/env python

a,b=map(int,input().split())
li=[]
for _ in range(a):
    word = int(input())
    li.append(word)
cnt=0
i=a-1
while True:
    if b>=li[i]:
        cnt+=1
        b-=li[i]
    elif b==0:
        print(cnt)
        break
    else:
        i-=1
