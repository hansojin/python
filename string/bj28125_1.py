#!/usr/bin/env python

import sys
input= sys.stdin.readline

n = int(input())
for _ in range(n):
    ch_arr = list(input().strip())

    pw_cnt = 0
    s_cnt = 0

    tmp = []
    for ch in ch_arr:
        if ch == '@':
            pw_cnt += 1
            tmp.append('a')
        elif ch == '[':
            pw_cnt += 1
            tmp.append('c')
        elif ch == '!':
            pw_cnt += 1
            tmp.append('i')
        elif ch == ';':
            pw_cnt += 1
            tmp.append('j')
        elif ch == '^':
            pw_cnt += 1
            tmp.append('n')
        elif ch == '0':
            pw_cnt += 1
            tmp.append('o')
        elif ch == '7':
            pw_cnt += 1
            tmp.append('t')
        elif ch == '\\':
            s_cnt += 1
        elif s_cnt == 1 and ch == '\'':
            s_cnt = 0
            pw_cnt += 1
            tmp.append('v')
        elif s_cnt == 1 and ch == '\\':
            s_cnt += 1
        elif s_cnt == 2 and ch == '\'':
            s_cnt = 0
            pw_cnt += 1
            tmp.append('w')
        else:
            tmp.append(ch)

    tlen = len(tmp)
    if tlen % 2 == 1:
        tlen += 1

    if tlen // 2 <= pw_cnt:
        print("I don't understand")
    else:
        print(''.join(tmp))

