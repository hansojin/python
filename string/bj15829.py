#!/usr/bin/env python

n=int(input())
word=str(input())
sum=0
cnt=0
for i in word:
    num=ord(i)-96
    sum+=num*31**(cnt)
    cnt+=1
print(sum%1234567891)

