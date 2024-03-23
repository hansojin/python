select round(avg(
    case when length is not null then length
    else 10 
    end),2) as AVERAGE_LENGTH
from fish_info
