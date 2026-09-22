CREATE TABLE    NewOrders (
    orderid     NUMBER,
    custid      NUMBER  NOT NULL,
    bookid      NUMBER  NOT NULL,
    saleprice   NUMBER,
    orderdate   DATE,
    PRIMARY KEY(orderid),
    FOREIGN KEY(custid) REFERENCES NewCustomer(custid) ON DELETE CASCADE
);