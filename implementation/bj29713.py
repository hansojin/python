#!/usr/bin/env python

bs= ["R","E","B","O","N","Z","S","I","L","V"]

n=int(input())
word=input()
cnt=[0]*len(bs)

for i in word:
    if i in bs:
        idx=bs.index(i)
        cnt[idx]+=1
cnt[0]//=2
cnt[1]//=2

print(min(cnt))

