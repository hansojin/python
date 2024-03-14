SELECT a.FLAVOR
from ICECREAM_INFO a
    join FIRST_HALF b
    on a.FLAVOR = b.FLAVOR
    where b.TOTAL_ORDER>3000
        and a.INGREDIENT_TYPE='fruit_based'
    order by b.TOTAL_ORDER desc
