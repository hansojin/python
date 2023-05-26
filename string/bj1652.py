#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[]
n=int(input())
for i in range(n):
    tmp=input()
    li.append(tmp)

new_li=list(map(list,zip(*li[::-1])))
one_li=[]
for i in new_li:
    one_li.append("".join(i))
def count(li):
    cnt=0
    for i in range(n):
        mt=li[i].rstrip().split('X')
        for j in mt:
            if len(j)>=2:
                cnt+=1
    return cnt

print(count(li),count(one_li))
