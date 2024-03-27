select * from places
where HOST_ID in (select HOST_ID
from PLACES 
group by HOST_ID
having count(*)>=2)
