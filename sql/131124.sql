SELECT a.MEMBER_NAME, REVIEW_TEXT, left(REVIEW_DATE,10) as REVIEW_DATE
from MEMBER_PROFILE a
join REST_REVIEW b
on a.MEMBER_ID=b.MEMBER_ID
where a.MEMBER_ID=(select a.MEMBER_ID 
                 from MEMBER_PROFILE a
                join REST_REVIEW b
                on a.MEMBER_ID=b.MEMBER_ID
                group by a.MEMBER_ID
                order by count(*) desc
                 limit 1)
order by REVIEW_DATE,REVIEW_TEXT
