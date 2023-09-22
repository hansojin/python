#!/usr/bin/env python

s=set()
s.add(' ')
n=int(input())
nl = input().split()
for i in range(len(nl)):
    s.add(nl[i])
m=int(input())
ml = input().split()
for i in range(len(ml)):
    s.add(str(ml[i]))
k=int(input())

kl = input()
for i in range(len(kl)):
    s.discard(kl[i])
ss=int(input())
word= input()

def sp(word,spl):
    res, now = [],[]
    for char in word:
        if char in spl:
            if now:
                res.append(''.join(now))
                now=[]
        else:
            now.append(char)
    if now:
        res.append(''.join(now))
    return res

ans = sp(word,s)
for i in ans:
    print(i)
