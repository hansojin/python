select a.ITEM_ID,ITEM_NAME,RARITY
from ITEM_INFO a
left join ITEM_TREE b
on a.ITEM_ID=b.PARENT_ITEM_ID
where PARENT_ITEM_ID is null
order by ITEM_ID desc
