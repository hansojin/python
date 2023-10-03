import sys
input= sys.stdin.readline
N = int(input())
res = 0
x = 1
while x*x <= N:
    x += 1
    res +=1
print(res)
