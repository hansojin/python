### 사전 자료형 관련 메서드.
---
* 사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원함
	* 키 데이터만 뽑아서 리스트로 이용할 때는 __keys()__ 함수를 이용
	* 값 데이터만을 뽑아서 리스트로 이용할 때는 __values()__ 함수를 이용

```
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])
```
실행결과
```
> dict_keys(['사과', '바나나', '코코넛'])
> dict_values(['Apple', 'Banana', 'Coconut'])
> Apple
> Banana
> Coconut
```