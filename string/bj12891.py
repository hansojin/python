#!/usr/bin/env python

from collections import deque

s,p =map(int,input().split())
dna = list(str(input()))
a,c,g,t=map(int,input().split())

dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
l,r = 0,p-1

q=deque(dna[l:r])
for i in q:
    dic[i]+=1

cnt=0

while r<s:
    dic[dna[r]]+=1
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        cnt+=1

    dic[dna[l]]-=1
    l+=1
    r+=1
print(cnt)
