#!/usr/bin/env python

import sys
input= sys.stdin.readline

hash_table = [ 0 for _ in range(1000)]

def hash_f(key):
    return hash(key)%1000

def set_data(key,value):
    hash_v = hash_f(key)
    hash_table[hash_v] = value

def get_data(key):
    hash_v=hash_f(key)
    print(hash_table[hash_v])

for _ in range(int(input())):
    st = list(map(int,input().split()))
    if st[0]==1:
        set_data(st[2],st[1])
    elif st[0]==2:
        get_data(st[1])
