#!/usr/bin/env python

n=int(input())
ppl=[]
for _ in range(n):
    a,b=map(int,input().split())
    ppl.append(a)
    ppl.append(b)
    # ppl.append(list(map(int,input().split())))

score=[1 for i in range(n)]
for i in range(n):
    for j in range(n):
        if ppl[2*i]<ppl[2*j] and ppl[2*i+1]<ppl[2*j+1]:
            score[i]+=1

for i in range(n):
    print(score[i],end=' ')

