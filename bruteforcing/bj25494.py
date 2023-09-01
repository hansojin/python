#!/usr/bin/env python

for _ in range(int(input())):
    A,B,C=map(int,input().split())
    ans=0
    for a in range(1,A+1):
        for b in range(1,B+1):
            for c in range(1,C+1):
                if a%b==b%c==c%a:
                    ans+=1
    print(ans)
