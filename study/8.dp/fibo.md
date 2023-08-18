```
# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
```

- 피보나치 수열의 시간 복잡도 : O(2ᴺ)

- 피보나치 수열의 효율적인 해법 : ** 다이나믹 프로그래밍**


