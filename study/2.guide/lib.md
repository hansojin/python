### 실전에서 유용한 표준 라이브러리
---
* 내장 함수: 기본 입출력 함수 부터 정렬 함수까지 기본적인 함수들을 제공
	* 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있음
* itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공
	* 특히 순열의 조합 라이브러리는 코딩 테스트에서 자주 사용됨
* heapq: 힙(Heap) 자료구조를 제공
	* 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
* bisect: 이진 탐색(Binary Search) 기능을 제공
* collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함
* math: 필수적인 수학적 기능을 제공함
	* 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함

---
#### 순열과 조합
* __순열__ : 서로 다른 𝑛개에서 서로 다른 𝑟개를 선택하여 일렬로 나열하는 것 : __nPr__
	* {'A', 'B', 'C'}에서 세 개를 선택하여 나열하는 경우: 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
```
from itertools import permutations
data = ['A', 'B', 'C'] 
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)
```
실행결과
```
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```
  
* __조합__ : 서로 다른 𝑛개에서 순서에 상관 없이 서로 다른 𝑟개를 선택하는 것 : __nCr__
	* {'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우: 'AB', 'AC', 'BC'
```
from itertools import combinations
data = ['A', 'B', 'C'] 
result = list(combinations(data, 2))
result2 = list(combinations(data, 3))
print(result)
print(result2)
```
실행결과
```
[('A', 'B'), ('A', 'C'), ('B', 'C')]
[('A','B', 'C')]
```
  
* __중복 순열과 중복 조합__ 
```
# 중복 순열
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) 
print('> 2개를 뽑는 모든 순열 구하기 (중복 허용)')
print(result)

# 중복 조합
from itertools import combinations_with_replacement
data = ['A', 'B', 'C'] 
result = list(combinations_with_replacement(data, 2)) 
print('> 2개를 뽑는 모든 조합 구하기 (중복 허용)')
print(result)
```
실행결과
```
> 2개를 뽑는 모든 순열 구하기 (중복 허용)
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
> 2개를 뽑는 모든 조합 구하기 (중복 허용)
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
``` 
  
* __Counter__ : 등장 횟수를 세는 기능을 제공함

```
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) 
print(counter['green']) 
print(dict(counter)) # 사전 자료형으로 반환
```
실행결과
```
3
1
{'red': 2, 'blue': 3, 'green': 1}
```
---

#### **global** 키워드
* global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고 함수 바깥에 선언된 변수를 바로 참조하게 됨
```
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)
```
실행결과
```
> 10
```

#### **여러 개의 반환 값**
```
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)

```
실행결과
```
> 10 4 21 2.3333333333333335
```

#### **람다** 표현식
* 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있음
	* 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징임

```
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

```
실행결과
```
> [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
> [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
```
```
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))

```
실행결과
```
> [7, 9, 11, 13, 15]
```


#### 최대 공약수와 최소 공배수
* 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd() 함수를 이용할 수 있음
```
import math
# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)
a = 21
b = 14
print(math.gcd(21, 14)) 	# 최대 공약수(GCD) 계산
print(lcm(21, 14)) 		# 최소 공배수(LCM) 계산
```
실행결과
```
7
42
```


