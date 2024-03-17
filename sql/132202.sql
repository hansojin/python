SELECT MCDP_CD as '진료과코드', count(*) as '5월예약건수'
from APPOINTMENT 
where left(APNT_YMD,7)='2022-05'
group by MCDP_CD
order by count(*), MCDP_CD

