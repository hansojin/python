select YEAR(SALES_DATE) as YEAR,
    MONTH(SALES_DATE) as MONTH,
    GENDER, count(distinct b.user_id) as USERS
from USER_INFO a
join ONLINE_SALE b
on a.USER_ID=b.USER_ID
group by YEAR, MONTH, GENDER
having GENDER is not null
order by year,month,gender
