#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import permutations

def cal2(fx,li):
    print(fx)
    tmp = eval(''.join(map(str,fx[:3])))
    for i in range(3,len(fx),2):
        tmp=eval(str(tmp).join(map(str,fx[i:i+2])))
        print(tmp)
    return tmp
def cal(fx):
    tmp=str(eval(''.join(map(str,fx[:3]))))
    for i in range(3,len(fx),2):
        tmp+=fx[i]+str(fx[i+1])
        tmp=eval(tmp)
    return tmp

n=int(input())
li=list(map(int,input().split()))
oper=list(map(int,input().split()))
sign=['+','-','*','//']
op=[]
for o in range(4):
    for cnt in range(oper[o]):
        op.append(sign[o])
maxx,minn=-1e9,1e9
for tup in permutations(op,n-1):
    case = list(tup)
    fx=[]
    for i in range(n-1):
        fx.append(li[i])
        fx.append(case[i])
    fx.append(li[n-1])
    nn=int(cal(fx))
    if nn>maxx:
        maxx=nn
    if nn<minn:
        minn=nn

print(maxx)
print(minn)
