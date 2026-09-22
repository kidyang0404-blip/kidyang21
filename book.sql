SELECT * FROM Book
INSERT INTO Book(bookid, bookname, publisher, price)
VALUES (11, '스포츠 의학', '한솔의학서적', 90000);

INSERT INTO Book(bookid, bookname, price, publisher)
       SELECT bookid, bookname, price, publisher
       FROM Imported_book;
       
UPDATE Customer
SET    address = '대한민국 부산'
WHERE  custid = 5;  

UPDATE Customer
SET    address = (
           SELECT address 
           FROM   Customer 
           WHERE  name = '김연아'
       )
WHERE  name = '박세리';

SELECT bookid, REPLACE(bookname,'야구', '농구') bookname, publisher, price
FROM   Book



SELECT   name "이름", NVL(phone, '연락처 없음') "전화번호"
FROM     Customer;
