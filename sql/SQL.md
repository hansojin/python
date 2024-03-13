#### DML(Data Manipulation Language)
- insert
- update
- delete
- select

#### DDL(Data Definition Language)
- create
- alter
- drop
- truncate
- rename

#### DCL(Data Control Language)
- grant
- revoke

#### TCL(Transaction Control Language)
- commit
- rollback
- savepoint

---

#### select

```
SELECT 열_이름
	FROM 테이블_이름
	WHERE 조건식
	GROUP BY 열_이름
	HAVING 그룹 조건식
	ORDER BY 열_이름
	LIMIT 숫자
```

* AND OR 
* Between N AND M
* 열이름 in ('a','b','c')
* LIKE + _ (한글자 매치) / %(0글자 이상 매치)
* LIMIT 3,2 == LIMIT 2 OFFSET 3 (=3번째 데이터부터 2개 조회)
* DISTINCT 중복제거
* 집계함수 _ sum, avg, min, max, count, count(distinct)

#### insert

```
insert into 테이블 values();
```

#### update

```
update 테이블 
    set 칼럼="값" 
    where 조건;
```

#### delete
```
delete from 테이블 
    where 조건;
```


#### CREATE : 테이블 생성

```
create table 테이블명(
    칼럼명 타입 조건,
    칼럼명 타입 조건,
    primary key 칼럼명
);
```

#### INSERT : 테이블에 데이터 삽입

```
insert into 테이블명 values();
insert into 테이블명 (열1,2...) value(값1,2...);
```

---
#### JOIN + ON

```
SELECT A.a, A.b, B.c 
FROM A
JOIN B
ON B.a = A.c;
```

* left/right outer join 
* cross join

#### CASE WHEN

```
CASE WHEN 칼럼=조건 THEN 결과
    WHEN 칼럼=조건 THEN 결과
    ELSE 결과 (else는 optional)
    END AS [칼럼명]
```



#### 문자 조작 함수

- UPPER(str) : 대문자 변환
- LOWER(str) : 소문자 변환
- INITCAP(str) : 첫 글자만 대문자로 변환
- CONCAT(str, tmp) : 두 문자값 결합
- SUBSTR(str,a,b) : 문자 추출 a = 시작위치, b = 개수
- LENGTH(str) : 문자열 길이 반환
- LEFT(str,N) : 문자열에서 왼쪽에서 N 문자만큼 반환 
- RIGHT(str,N) : 문자열에서 오른쪽에서 N 문자만큼 반환 
- FLOOR(), CEIL(), ROUND() : 내림, 올림, 반올림
- SQRT(), POW(a,b), EXP(), LOG() : 제곱근,a^b, e의 거듭제곱, 자연로그 값
- SIN(), COS(), TAN(), ABS(), RAND()
- NOW(), CURDATE(), CURTIME() : YYYYMMDDHHMMSS, YYYY-MM-DD, HH:MM:SS
- DATE(), MONTH(), DAY(), HOUR(), MINUTE(), SECOND() : date(now())로 사용
- L/RPAD(대상,총길이,채울문자열) : 대상 문자열에 채울문자열을 총길이만큼 채워서 반환
- LPAD('001',7,'0') ▶ 0000001
- LTRIM, RTRIM(대상, 제거할 문자열) : 대상 문자열에서 제거할 문자열을 없앤 뒤 반환
- select LTRIM('00010' , '00') ▶ 010
- REPLACE(대상문자열,바꾸고싶은대상,바꾸고싶은내용) : 대상문자열에서 바꾸고 싶은 대상을 바꾸고 싶은 내용으로 수정한 뒤 반환
- REPLACE('ABCDEFG','DEF','XXX') ▶ ABCXXXG
- 한글로만된 결과 찾기 ▶ WHERE 칼럼명 REGEXP '[가-힣]'; 
