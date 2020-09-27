### Basic UI/UX Elements Tested

#### Body Styling
```css
body {
	padding: 30px 30px;
	font-family: sans-serif;
	background-color: orange
}
```
#### Creation of Tables
```html
<table>
	<tr>
		<th>Heading 1</th>
		<th>Heading 2</th>
	</tr>
	<!-- Looping through data with jinja to form table rows-->
	{% for item in data %}
	<tr>
		<td>{{ item[0] }}</td>
		<td>{{ item[1] }}</td>
	</tr>
	{% endfor %}
</table>
```
Let's style the tables
```css
table, th, td {
	border: 2px solid grey;
	padding: 10px;
	text-align: center;
}

table {
  border-collapse: collapse;
  width: 100%; /*makes table occupy full space*/
}	
```
#### Creation of Forms
```html
 <form method="post" action="/">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label><br>
  <input type="submit">
</form> 
```

##### Closing tag(s) not needed in input boxes
<img.../>, <input.../>  and <br.../> are _void elements_ thus they can be close with `>` or `/>`


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

### Uploading files
Backend python
```python
....
from werkzeug.utils import secure_filename
....
app.config['SECRET_KEY'] = '9483f' #random
app.config['UPLOAD_FOLDER'] = 'static/'

f = request.files['bigpic']
filenames = []
if f:
    f_name = secure_filename(f.filename)
    filenames.append(f_name)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))

return render_template("upload.html", filenames=filenames)
```
html page
```html
<form action="/upload" method="post" enctype="multipart/form-data">
	<input type="file" name="bigpic"/>
	<input type="submit"/>
</form>
{% for filename in filenames %}
<div>
	<img src="{{ url_for('static', filename=filename) }}">
</div>
{% endfor %}
```
`multipart/form-data` is necessary to ensure no characters when uploading files are encoded. 

Default value tends to be `application/x-www-form-urlencoded ` which encodes data


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

### Miscellaneous

Select Distinct Records
```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
```
_MAX(), MIN(), SUM() are applied similarly as shown above_

Order By ASC or DESC
```sql
SELECT col1, col2, ...
FROM table_name
ORDER BY col1, col2, ... ASC; 
```

Update
```sql
UPDATE table_name
SET col1 = val1, ...
WHERE condition; 
```
