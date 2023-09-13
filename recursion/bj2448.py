#!/usr/bin/env python

n = int(input())

graph = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]


def star(N, bf):
    af = [[" "] * (2 * 2 * N - 1) for _ in range(2 * N)]
    for i in range(N):
        af[i][N:N+2*N-1] = bf[i]

    k = 0
    for i in range(N, 2 * N):
        af[i][:2*N] = bf[k]
        af[i][2*N:2*N+len(bf[k])] = bf[k]
        k += 1

    if 2*N == n:
        return af

    return star(2*N, af)


if n==3:
    res = graph
else:
    res = star(3, graph)

for i in res:
    print("".join(i))
