SELECT 
    left(PRODUCT_CODE,2) as CATEGORY,
    count(*) as PRODUCTS
from PRODUCT
group by CATEGORY
