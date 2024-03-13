```
select * from city; 

select *
from city
where Population < 8000000
    and Population > 7000000;

select *
from city
where CountryCode = 'KOR'
    and Population >= 1000000;

select *
from city
where Population between 7000000 and 8000000;

select *
from city
where Name In('Seoul', 'New York', 'Tokyo');

select *
from city
where CountryCode like 'KO_';

select *
from city
where Name like 'Tel %';

-- SUBQUERY
select *
from city
where CountryCode = (
    select CountryCode
    from city
    where Name = 'Seoul');

-- ANY = SOME 동일한 의미로 사용
select *
from city
where Population > ANY (
    select Population
    from city
    where District = 'New York');

- ALL : 서브쿼리 결과를 모두 만족해야함
select *
from city
where Population > all (
    select Population
    from city
    where District = 'New York');

select *
from city
order by CountryCode ASC, Population DESC;

select distinct CountryCode
from city
order by Population desc
limit 10;

select count(*)
from city;

select CountryCode, max(Population) as 'MAX' 
from city
group by CountryCode;

-- having : 그룹 조건
select CountryCode, max(population)
from city
group by CountryCode
having max(Population) > 8000000;

-- GROUP BY절과 함께 with rollup문 사용 : 총합 또는 중간합계가 필요한 경우 사용
select CountryCode, Name, sum(population)
from city
group by CountryCode, Name with rollup;

-- JOIN + ON
select *
from city
join country ON city.CountryCode = country.Code 
join countrylanguage ON city.CountryCode = countrylanguage.CountryCode;











```