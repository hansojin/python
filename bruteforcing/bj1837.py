#!/usr/bin/env python

p,k=map(int,input().split())

def primeList(n):
    n+=1
    si = [False,False] + [True]*(n)
    end=int(n**0.5)+1

    for i in range(2,end):
        if si[i]==True:
            for j in range(i+i,n,i):
                si[j]=False
    return [i for i in range(n) if si[i]==True]

li = primeList(p)

for i in li:
    for j in li:
        if i*j==p:
            if i>k and j>k:
                print("GOOD")
                exit()
            else:
                print("BAD",end= " ")
                print(i)
                exit()

