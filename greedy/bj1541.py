#!/usr/bin/env python

li=input().split('-')   # - 기준으로 나누기

num=[]

for i in li:
    sum=0
    tmp=i.split('+')    # 그안에서 +끼리 묶인게 있다면
    for j in tmp:
        sum+=int(j)     # 더해서
    num.append(sum)     # num list에 넣어두기
n=num[0]                # 어차피 첫 숫자는 + 니까

for i in range(1,len(num)):
    n-=num[i]           # 그 이후 num 부터 첫번째 숫자에서 빼주기
print(n)                # 최소를 만들어 줄거니까
