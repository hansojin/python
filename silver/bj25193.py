#!/usr/bin/env python

n=int(input())
food= input()
cnt=0
for i in range(len(food)):
    if food[i]=='C':
        cnt+=1
if cnt%(n-cnt+1)!=0:
    tmp=1
else:
    tmp=0
print(cnt//(n-cnt+1) + tmp)
