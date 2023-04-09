#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
dic={}

for i in range(n):
    word=input()
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1

list=[]
num=max(dic.values())

for i in dic:
    if num==dic[i]:
        list.append(i)
list.sort()
print(list[0])
