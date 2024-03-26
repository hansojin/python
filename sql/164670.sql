SELECT b.USER_ID, b.NICKNAME,
    concat(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) as '전체주소',
    concat(left(TLNO,3),'-',substring(TLNO,4,4),'-',right(TLNO,4)) as '전화번호'
from USED_GOODS_BOARD a
join USED_GOODS_USER b
on a.WRITER_ID=b.USER_ID
group by b.USER_ID
having count(*)>=3
order by b.USER_ID desc
