select count(*) as FISH_COUNT, Month(TIME) as MONTH
from FISH_INFO 
group by MONTH
order by MONTH
