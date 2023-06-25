#!/usr/bin/env python

def least_integer(x):
    return int(x) if x.is_integer() else int(x) + 1

T = int(input())  

for _ in range(T):
    S = input()  

    n = len(S)
    prefix_length = least_integer(n / 3)
    s_prime = S[:prefix_length]
    rev_s_prime = s_prime[::-1]
    tail_s_prime = s_prime[1:]
    tail_rev_s_prime = rev_s_prime[1:]

    if S == s_prime + rev_s_prime + s_prime or S == s_prime + tail_rev_s_prime + s_prime or \
       S == s_prime + rev_s_prime + tail_s_prime or S == s_prime + tail_rev_s_prime + tail_s_prime:
        print(1)  
    else:
        print(0)  

