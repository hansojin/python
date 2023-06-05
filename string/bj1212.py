#!/usr/bin/env python

'''
n=str(input())
n=n[::-1]
num=0
for i in range(len(n)):
    num+=(8**i)*int(n[i])
li=[]
while True:
    li.append(num%2)
    num=num//2
    if num==1:
        li.append(1)
        break
for i in li[::-1]:
    print(i,end='')
'''
print(bin(int(input(), 8))[2:])

