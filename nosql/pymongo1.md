## Initializing the Database
### Imports
```python
from pymongo import MongoClient
import json
```

### Connecting to a Database
```python
client = MongoClient('localhost',27017)
clidb = client.customer
clicol = client.customer.results
clidb = client['customer'] #alternative
clicol = client['customer']['results'] #alternative
```
### Input of items

json.load() is for loading a file,json.loads() works with strings

### JSON formats (looking for more wierd ones)
Ideal file format 
```json
[
{"address": 
    {"building": "1007"}
},
{"address": 
    {"building": "534"}
},
{"address": 
    {"building": "9668"}
}]
```
- If there are no front brackets, add them!

- If there are missing commas, like below:
```json
{"address": {"building": "1007"}}
{"address": {"building": "534"}}
{"address": {"building": "9668"}}
```
it will be too tedious to add commas, especially for larger databases. Inserting them one by one would be more wise, I think
```python
with open('_______.json') as f:
for line in f:
    file_data = json.loads(line)
    x = mycol.insert_one(file_data)
    print(x.inserted_ids)
```
#### Example Json File (Needs opening and and closing brackets, as well as commas in between)

```json
[{"CustName":"Molly Chua", "CustHP":"87654220"},

{"CustName":"Daren Ng", "CustHP":"91134528",
    "Request":[{"Date":"20190917","DriverName":"Andrew Yap","DriverHP":"85331729"}]}]
```

##### Inserting Data
```python
hcicol.insert_one({"CustName":new_name, "CustHP":new_hp,
    "Request":[{"Start":start,"End":end, "Cost":cost, "Time":time, "Date":date,"DriverName":driver_n,"DriverHP":driver_hp}]})

```

## Query and Projection OperaTORS

##### Finding Data
```python
db.collection.find(query, projection)
clicol.find({},{"CustName":1,"_id":0})
```

#### Comparison
|Name|	Description                                                        |
|:-------------:| --------------------------------------------------------:|
|$eq |	Matches values that are equal to a specified value.                |
|$gt |	Matches values that are greater than a specified value.            |
|$gte|	Matches values that are greater than or equal to a specified value.|
|$in |	Matches any of the values specified in an array.                   |
|$lt |	Matches values that are less than a specified value.               |
|$lte|	Matches values that are less than or equal to a specified value.   |
|$ne |	Matches all values that are not equal to a specified value.        |
|$nin|	Matches none of the values specified in an array.                  |


#### Logical
|Name	|Description 
|:-------------:| ------------------------------------:|
|$and	|Joins query clauses with a logical AND returns all documents that match the conditions of both clauses.|
|$not	|Inverts the effect of a query expression and returns documents that do not match the query expression.|
|$nor	|Joins query clauses with a logical NOR returns all documents that fail to match both clauses.  |
|$or|	Joins query clauses with a logical OR returns all documents that match the conditions of either clause. |
