#!/usr/bin/env python

a,b=map(int,input().split())
li=list()
for _ in range(a):
    li.append(int(input()))


cnt=0
for i in reversed(range(a)):
    cnt+=b//li[i]
    b=b%li[i]
'''
a 역순 _ reversed() 사용
cnt는 b를 list역순대로 나눈 몫을 더해주고,
b는 그 나눈 값의 나머지로 for문내에서 순차적으로 계산됨
'''
print(cnt)
