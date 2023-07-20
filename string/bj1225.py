#!/usr/bin/env python

n,m=map(str,input().split())
sum,tmp=0,0
for i in n:
    tmp+=int(i)
    // 2중포문쓰면 시간 초과
    // a*d + b*d + c*d 는 (a+b+c)*d

for j in m:
    sum+=tmp*int(j)
print(sum)
