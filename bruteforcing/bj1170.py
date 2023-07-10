#!/usr/bin/env python

for i in range(int(input())):
    srt,end=map(int,input().split())
    cnt=0
    for i in range(srt,end+1):
        i=str(i)
        for j in i:
            if j=='0':
                cnt+=1
    print(cnt)
