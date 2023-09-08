#!/usr/bin/env python

from string import ascii_lowercase

alpha,copy={},{}
for _ in range(int(input())):
    flag=True
    for i in ascii_lowercase:
        alpha[i]=0
        copy[i]=0

    word, cpy = map(str,input().split())
    if len(word)!=len(cpy):
        flag = False
        break
    else:
        for i in range(len(word)):
            alpha[word[i]]+=1
            copy[cpy[i]]+=1
    
        for i in ascii_lowercase:
            if alpha[i]!=copy[i]:
                flag=False
                break
    if flag==False:
        print("Impossible")
    else:
        print("Possible")
