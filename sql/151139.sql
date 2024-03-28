select month(START_DATE) as MONTH,CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where month(START_DATE) between 8 and 10
    and car_id in (
        select car_id 
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where month(START_DATE) between 8 and 10
        group by CAR_ID 
        having count(*)>=5
    )
group by month, CAR_ID
order by month, CAR_ID desc

