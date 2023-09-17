#!/usr/bin/env python

import sys
input =sys.stdin.readline

n=int(input())
li=[]
for _ in range(n):
    li.append(int(input()))
li.sort(reverse=True)

if n>42:
    del li[42:]


five = [k for k in li if k>=250]
four = [k for k in li if 200<=k<250]
three = [k for k in li if 140<=k<200]
two = [k for k in li if 100<=k<140]
one = [k for k in li if 60<=k<100]

print(sum(li), len(five)*5+len(four)*4 + len(three)*3 + len(two)*2 + len(one)*1)




