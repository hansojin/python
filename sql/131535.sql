SELECT count(*) as USERS
from USER_INFO
where left(joined,4)='2021' 
    and Age between 20 and 29;
