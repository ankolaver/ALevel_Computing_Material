#HCI NOSQL

from pymongo import MongoClient
import json
import time

client = MongoClient('localhost',27017)
hcidb = client.hci_customer
hcicol = client.hci_customer.results
#hcidb = client['hci_customer'] #alternative
#hcicol = client['hci_customer']['results'] #alternative

'''
#Task1
#json.load() is for loading a file,json.loads() works with strings
with open('CUSTOMER.json') as f:
    f = json.load(f)
    for line in f:
        print(line)
        print("Inserting####...", end="\n")
        x = hcicol.insert_one(line)
        print(x.inserted_id)
        
'''
'''
#Task1.2
#print only certain field in ascending order
#.sort([("field1", 1), ("field2", -1)])
query = hcicol.find({},{"CustName":1,"CustHP":1,"_id":0}).sort("CustName",1)#ascending
for items in query:
    print(items)
'''

'''
#Task2
#print particular day
year = input("Enter a Year: ")
month = input("Enter a Month: ")
day = input("Enter a Day: ")
chosen_date = str(year+month+day)
dayquery = {"Request.Date":{"$eq":chosen_date}}
if hcicol.count_documents(dayquery) > 0:
    print("There are",hcicol.count_documents(dayquery),"such documents on",chosen_date)
else:
    print("No such documents found on",chosen_date)
'''

#Task3
#add membership points
'''Jason Lim with phone number 8720 9133 took a trip from "Mapletree Business
Centre" to "Changi Airport" at 9am on 20 Sep 2019, with a cost of $20.4.
The driver was Helen Hu with phone number 9254 6710'''
new_record = input("Enter a new request: ")
new_name = ' '.join(i for i in new_record.split(" ")[:2])
new_hp =  ' '.join(i for i in new_record.split(" ")[5:7])
start = new_record.replace("\"","^^").split("^^")[1]
end =  new_record.replace("\"","^^").split("^^")[3]
cost =  new_record.replace(". ","$").split("$")[1]
time = "0900"
date = "200902019"
driver_n = ' '.join(i for i in new_record.split(" ")[31:33])
driver_hp = ' '.join(i for i in new_record.split(" ")[36:])

#db.collection.find(query, projection)
namequery = hcicol.find({},{"CustName":1,"_id":0})
currnames = []
for items in namequery:
    currnames.append(items["CustName"])
print(currnames)

'''
#check if name already exists
if new_name not in currnames:
    y = hcicol.insert_one({"CustName":new_name, "CustHP":new_hp,
    "Request":[{"Start":start,"End":end, "Cost":cost, "Time":time, "Date":date,"DriverName":driver_n,"DriverHP":driver_hp}]})
    
    print(y.inserted_id)
'''

indivpoints = 0
pointscalc = hcicol.find({"CustName":{"$eq":"Jason Lim"}},{"_id":0,"Request.Cost":1})
for point in pointscalc:
    indivpoints+=float(point['Request'][0]['Cost'])


if 300<=indivpoints<=1200:
    print("Silver")
elif 1200<=indivpoints<=4500:
    print("Gold")
elif indivpoints>4500:
    print("Premium")
else:
    print("Member")
