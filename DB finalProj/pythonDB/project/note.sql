select * from XXX               
選出指定的欄位

select distinct [name] from XXX 
重複的不要出現

sel... * from XXX where         
縮小範圍 = >= ... between(第32 前面可以加not) like(第28 前面可以加not) 

sel......f....w...=...  and ...=...  
就and/or

SELECT Company, OrderNumber FROM Orders ORDER BY Company asc, OrderNumber desc
Company排數字 name排字母  順向:asc 逆向加上desc

INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
插入 加入 值

UPDATE Person SET FirstName = 'Fred' WHERE LastName = 'Wilson' 
UPDATE 表名稱 SET 列名稱=new值  WHERE 列名稱=值

DELETE FROM Person WHERE LastName = 'Wilson'
刪除某行ㄉ值

SELECT TOP 2 * FROM Persons
選中最上面的兩條內容    /   top 2 也可以改成 => top 50 percent  (用%數來表示)

SELECT * FROM Persons WHERE City LIKE 'N%'
選中某city  字串N後面隨便 全都可以當作目標選中
可以加入 not   like=> not like  不要包含n%的city名字

SELECT * FROM Persons WHERE LastName BETWEEN 'Adams' AND 'Carter'
以字母顺序显示介于 "Adams"（包括）和 "Carter"（不包括）之间的人

SELECT * FROM Persons WHERE FirstName LIKE '_eorge'
第一個字隨便 希望後面接下去的是eorge 的name  底線

X SELECT * FROM Persons WHERE City LIKE '[!ALN]%'
X "Persons" 表中选取居住的城市不以 "A" 或 "L" 或 "N" 开头的人  !代表相反(沒有!也行)
X 指定開頭

SEL... column_name(s) F... table_name W... column_name IN (value1,value2,...)
EX: SELECT * FROM Persons WHERE LastName IN ('Adams','Carter')
中选取姓氏为 Adams 和 Carter 的人 指定姓氏



SELECT po.OrderID, p.LastName, p.FirstName
FROM Persons AS p, Product_Orders AS po
WHERE p.LastName='Adams' AND p.FirstName='John'
as的用法


CREATE DATABASE my_db 
希望创建一个名为 "my_db" 的資料庫

CREATE TABLE Persons
(
Id_P int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
)
建立一個entity (table)


NOT NULL 
約束強製字段始終包含值。這意味著，如果不向字段添加值，就無法插入新記錄或者更新記錄。

unique
primary= unique + not NULL
 

CREATE INDEX Index_Pers ON Person (LastName) 
給個index
ALTER TABLE table_name DROP INDEX index_name
撤掉index

DROP TABLE     删除表
DROP DATABASE  删除資料庫

ALTER TABLE Persons ADD Birthday date
在表 "Persons" 中添加一个名为 "Birthday" 的新列。
ALTER TABLE Persons ALTER COLUMN Birthday varchar(10)
改变 "Persons" 表中 "Birthday" 列的数据类型。


NOW()	        返回当前的 日期和时间
CURDATE()	    返回当前的 日期
CURTIME()	    返回当前的 时间
DATE()	        提取日期或日期/时间表达式的日期部分
EXTRACT()	    返回日期/时间按的单独部分
DATE_ADD()	    给日期添加指定的时间间隔
DATE_SUB()	    从日期减去指定的时间间隔
DATEDIFF()	    返回两个日期之间的天数
DATE_FORMAT()	用不同的格式显示日期/时间

DATE - 格式 YYYY-MM-DD
DATETIME - 格式: YYYY-MM-DD HH:MM:SS
TIMESTAMP - 格式: YYYY-MM-DD HH:MM:SS
YEAR - 格式 YYYY 或 YY


SELECT LastName,FirstName,`Address` FROM Persons WHERE Address IS NULL
查詢含有空值的欄位 is null => is not null





function---------------
SELECT function(列) FROM 表


SELECT AVG(OrderPrice) AS OrderAverage FROM Orders
求出平均    欄位           輸出的結果欄位名字   表


SELECT Customer FROM Orders 
WHERE OrderPrice>(SELECT AVG(OrderPrice) FROM Orders)
希望找到 OrderPrice 值高于 OrderPrice 平均值的客户。


SELECT COUNT(column_name) FROM table_name
            (distinct c.._name)

SELECT COUNT(Customer) AS CustomerNilsen FROM Orders
WHERE Customer='Carter' 
計算 叫做"Carter"的這個人 的订单数          

FIRST() 函數返回指定的字段中第一個記錄的值。

LAST() 函數返回指定的字段中最後一個記錄的值。

MAX() 函數返回一列中的最大值。NULL 值不包括在計算中。

MIN() 函數返回一列中的最小值。NULL 值不包括在計算中。

SUM() 函數返回數值列的總數（總額）。

GROUP BY 语句用于结合合计函数，根据一个或多个列对结果集进行分组。
O_Id	OrderDate	OrderPrice	Customer
1	    2008/12/29	1000        Bush
2	    2008/11/23	1600        Carter
3	    2008/10/05	700	        Bush
4	    2008/09/28	300	        Bush
5	    2008/08/06	2000        Adams
6	    2008/07/21	100	        Carter
SELECT Customer,SUM(OrderPrice) FROM Orders GROUP BY Customer 之後就會↓↓↓
Customer	SUM(OrderPrice)   
Bush	    2000
Carter	    1700
Adams	    2000





在SQL 中增加HAVING 子句原因是，WHERE 關鍵字無法與合計函數一起使用。

SELECT Customer,SUM(OrderPrice) FROM Orders
GROUP BY Customer
HAVING SUM(OrderPrice)<2000
查找订单总金额少于 2000 的客户。




UCASE() 函數把字段的值轉換為大寫。

LCASE() 函數把字段的值轉換為小寫。

MID() 函數用於從文本字段中提取字符。

LEN() 函數返回文本字段中值的長度。

ROUND() 函數用於把數值字段舍入為指定的小數位數。

NOW() 函數返回當前的日期和時間。。

FORMAT() 函數用於對字段的顯示進行格式化。







