#!/usr/bin/env python

for _ in range(int(input())):
    li = [i for i in range(65,91)]
    for i in input():
        li[ord(i)-65]=0
    print(sum(li))
