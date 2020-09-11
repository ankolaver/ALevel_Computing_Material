### Inserting to the database
```python
import sqlite3
import csv

conn = sqlite3.connect("bakery.db")
cur = conn.cursor()

with open('CAKES.TXT') as f:
    items = csv.reader(f, delimiter=",")
    for line in items:
        #specify the tables to insert
        cur.execute("INSERT OR IGNORE INTO PRODUCT(ProductCode,Name,Location,Price) VALUES(?,?,?,?)",(line[0],line[1],line[2],float(line[3])))
        conn.commit()
        
        #insert to all tables if not specified
        cur.execute("INSERT OR IGNORE INTO CAKE VALUES(?,?,?)",(line[0],int(line[4]),line[5]))
        conn.commit()
    print("Success")
conn.close()
```
`OR IGNORE` is an optional clause; prevents duplicates due to errors when inserting

### Left Join or vice versa for RIGHT JOIN
<img src="https://user-images.githubusercontent.com/47784720/92840827-2aa1ee00-f414-11ea-88c0-1156d5f97202.jpg" alt="SQL Left Join" width="500"/>

select records from left and matching ones on the right

*Note: need not be primary key on left; just need to be matching fields*

```sql
SELECT Customers.CustomerName, Orders.OrderDate
FROM Orders
LEFT JOIN Customers
ON Orders.CustomerID=Customers.CustomerID
ORDER BY Orders.OrderDate;
```

Simplified with c as Customers and o as Orders

```sql
SELECT c.CustomerName, o.OrderDate
FROM Orders o
LEFT JOIN Customers c
ON o.CustomerID=c.CustomerID
ORDER BY c.CustomerName;
```

### Inner Join
<img src="https://user-images.githubusercontent.com/47784720/92840284-8029cb00-f413-11ea-82f1-6f914a63dffc.jpg" alt="SQL Inner Join" width="500"/>

selects records that have matching values in both tables
```sql
SELECT c.CustomerName, o.OrderID, o.OrderDate
FROM Customers c 
INNER JOIN Orders o ON o.CustomerID = c.CustomerID;
```
