select b.ANIMAL_ID, b.NAME
from ANIMAL_INS a
right join ANIMAL_OUTS b
on a.ANIMAL_ID=b.ANIMAL_ID
where a.NAME is null
and b.NAME is not NULL
order by ANIMAL_ID
