#!/usr/bin/env python

word = input()
alpha= 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in word:
        print(word.index(i), end=' ')
    else : 
        print(-1, end=' ')
