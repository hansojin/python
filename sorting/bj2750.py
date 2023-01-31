#!/usr/bin/env python

n=int(input())
numList=[]
for _ in range(n):
    # num=int(input())
    # numList.append(num)
    numList.append(int(input()))

# sortN=sorted(numList)
numList.sort()

# for i in range(n):
#    print(sortN[i])
for i in numList:
    print(i)

