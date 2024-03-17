
SELECT ANIMAL_TYPE, count(*) as count
from ANIMAL_INS 
group by ANIMAL_TYPE
having ANIMAL_TYPE in ('cat','dog')
order by ANIMAL_TYPE
