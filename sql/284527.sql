select sum(c.SCORE) as SCORE, 
	c.EMP_NO, b.EMP_NAME, b.POSITION, b.EMAIL
from HR_GRADE c
join HR_EMPLOYEES b
on b.EMP_NO=c.EMP_NO
group by c.EMP_NO
order by SCORE desc
limit 1
