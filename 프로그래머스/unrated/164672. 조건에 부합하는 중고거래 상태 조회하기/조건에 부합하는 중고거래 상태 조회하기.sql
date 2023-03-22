-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
CASE B.STATUS  
WHEN "SALE" THEN "판매중" 
WHEN "DONE" THEN "거래완료"
WHEN "RESERVED" THEN "예약중"
END 
FROM USED_GOODS_BOARD AS B
WHERE CREATED_DATE ='2022-10-05'
ORDER BY BOARD_ID DESC