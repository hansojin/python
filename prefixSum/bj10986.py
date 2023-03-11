#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))

subsum=0
remainder=[0]*m     #나머지가 같은 애들끼리 계산
                    #(a[j]-a[i])%m==0 은 a[j]%m=a[i]%m 으로 계산가능
for i in range(n):
    subsum+=a[i]
    remainder[subsum%m] +=1

cnt=remainder[0]    #애초에 나머지가 0인 애들은 혼자 뽑혀도 나눠지니까

for i in remainder:
    cnt += i*(i-1)//2  #i C 2

'''
cnt=0
s=e=0
subsum=a[s]
<2ptr>
while True:
    if e<n-1:
        e+=1
        subsum+=a[e]
        if subsum%m==0:
            cnt+=1
    else:
        s+=1
        if s==n-1:
            break
        subsum=a[s]
        if subsum%m==0:
            cnt+=1
        e=s
'''

print(cnt)



