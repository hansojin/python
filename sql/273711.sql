SELECT s1.ITEM_ID, s1.ITEM_NAME, s1.RARITY
FROM ITEM_INFO i2,
    (SELECT i1.ITEM_ID, t1.PARENT_ITEM_ID, i1.ITEM_NAME, i1.RARITY
    FROM ITEM_TREE t1, ITEM_INFO i1
    WHERE t1.ITEM_ID = i1.ITEM_ID) s1
WHERE s1.PARENT_ITEM_ID = i2.ITEM_ID
    AND i2.RARITY = "RARE"
ORDER BY s1.ITEM_ID DESC
