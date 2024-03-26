select c.APNT_NO,a.PT_NAME,a.PT_NO,c.MCDP_CD,b.DR_NAME,c.APNT_YMD
from APPOINTMENT c
join PATIENT a
    on a.PT_NO=c.PT_NO
join DOCTOR b
    on b.DR_ID=c.MDDR_ID
where c.MCDP_CD='CS'
    and APNT_YMD like '2022-04-13%'
    and APNT_CNCL_YN = 'N'
order by c.APNT_YMD
