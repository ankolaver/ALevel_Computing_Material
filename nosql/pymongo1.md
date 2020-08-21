## Initializing the Database
### Imports
```python
from pymongo import MongoClient
import json
import csv #if csv reader needed
```

### Connecting to a Database
```python
client = MongoClient('localhost',27017)
clidb = client.customer
clicol = client.customer.results
clidb = client['customer'] #alternative
clicol = client['customer']['results'] #alternative
```
### Pre-loading files

### JSON formats (looking for more wierd ones)
##### Ideal file format 
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
#### Example Json File (Needs opening and and closing brackets, as well as commas in between)

```json
[{"CustName":"Molly Chua", "CustHP":"87654220"},

{"CustName":"Daren Ng", "CustHP":"91134528",
    "Request":[{"Date":"20190917","DriverName":"Andrew Yap","DriverHP":"85331729"}]}]
```

## Inserting Data

### Function to convert between CSV and JSON
_takes each row as json entry_
```python
def csv_to_json(filepath,mainkey):
    with open(filepath) as file:
        reader = csv.DictReader(file)
        fin = []
        for row in reader:
            fin.append(row)
    
    with open(f'{filepath[:-4]}.json','w') as jsonf:
        jsonf.write(json.dumps(fin, indent=4))
    return fin
```
> json.load() is for loading a file, json.loads() works with strings
### Inserting Documents one by one
__It will be too tedious to add commas, especially for larger databases. Inserting them one by one would be more wise perhaps__
```python
with open('_______.json') as f:
    for line in f:
        file_data = json.loads(line)
        x = mycol.insert_one(file_data)
        print(x.inserted_ids)
```
__Inserting a Specific Document__
```python
hcicol.insert_one({"CustName":new_name, "CustHP":new_hp,
    "Request":[{"Start":start,"End":end, "Cost":cost, "Time":time, "Date":date,"DriverName":driver_n,"DriverHP":driver_hp}]})
```
### Inserting Many Documents
```python
def load_documents(mongocol,filepath):
    with open(filepath) as f:
        file_data = json.load(f)
        x = mongocol.insert_many(file_data)
        return x.inserted_ids
```
## Updating a database
```python
criteria = {"page_count": {"$exists": False}}
newValues = {"$set":{"page_count": 'Less Than 100 Pages'}}
bkCol.update_many(criteria, newValues)
```
## Query and Projection OperaTORS

#### Finding Data
```python
db.collection.find(query, projection)
clicol.find({},{"CustName":1,"_id":0})
```

#### Print in reverse/ascending order
```python
mydoc = mycol.find().sort("name") #ascending order
mydoc = mycol.find().sort("name", -1) #reverse order
```

### Comparison
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


### Logical
|Name	|Description 
|:-------------:| ------------------------------------:|
|$and	|Joins query clauses with a logical AND returns all documents that match the conditions of both clauses.|
|$not	|Inverts the effect of a query expression and returns documents that do not match the query expression.|
|$nor	|Joins query clauses with a logical NOR returns all documents that fail to match both clauses.  |
|$or|	Joins query clauses with a logical OR returns all documents that match the conditions of either clause. |

## [Pipeline](https://www.w3resource.com/mongodb/shell-methods/collection/db-collection-aggregate.php)


## MongoDB Shell Commands
|**Command**|**Description**|
|:-------------:|:------------------:|
|mongo|connect to local host 27017|
|help|get help|
|show dbs	|Showcase dbs in current|
|show collections	|Showcase collections in current database|
|use <database/column_name>	|Switch to a database/column name|
|db.collection.insert( <document> )|Inserting a new document in a collection|
|db.listCommands()|List Commands|
|db.<collection_name>.find().limit(5).pretty(); |Showcases 5 documents from collection. _pretty_ is meant to present in in JSON format|
