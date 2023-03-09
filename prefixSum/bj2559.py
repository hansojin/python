#!/usr/bin/env python

import sys
input = sys.stdin.readline

a,b=map(int,input().split())
li=list(map(int,input().split()))
lis=[]
lis.append(sum(li[:b])) # sliding window 처럼 일단 첫 slide는 만들어주기

for i in range(a-b):    # 앞ptr은 빼주고 뒷 ptr는 더해주기
    lis.append(lis[i]-li[i]+li[i+b])


print(max(lis))

