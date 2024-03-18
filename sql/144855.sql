SELECT a.CATEGORY, sum(b.SALES) as TOTAL_SALES
from BOOK a
join BOOK_SALES b
on b.BOOK_ID = a.BOOK_ID 
where b.SALES_DATE like '2022-01%'
group by a.CATEGORY
order by a.CATEGORY
