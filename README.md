##### Pancakes - Food for Computing Revision
## Algorithms

### Search 
- binary search
- linear search

### Sort (Iterative & recursive maybe soon...)
<img src="https://user-images.githubusercontent.com/47784720/84563618-74385980-ad8f-11ea-9bd1-cd3009df81bd.png" alt="time" width="750"/>

| Sorting Type   | Best         | Worse        |
| :------------: | :----------: | :----------: |
| bubble sort    | O(n)         | O(n^2)       |
| insertion sort | O(n)         | O(n^2)       |
| merge sort     | O(n log(n))  | O(n log(n))  |
| quick sort     | O(n log(n))  | O (n^2)      |
    
### [Datastructures](https://github.com/Kennethkcpdhs/Honey_Pancake/tree/master/Algorithms/datastructures)
- linkedlist 
- queue with array implementation
- queue with linkedlist implementation
- stack with array implementation
- stack with linked list implementation

### Classes
- Inheritance and encapsulation

## Web Apps (Flask)
- SQL
- [Reading from a file](https://github.com/Kennethkcpdhs/Honey_Pancake/blob/master/hci_webapp/app.py)

## [SQL](https://github.com/Kennethkcpdhs/Honey_Pancake/blob/master/sql/sql_help.md) 
## [NoSQL](https://github.com/Kennethkcpdhs/Honey_Pancake/blob/master/nosql/pymongo1.md#initializing-the-database)

## [Python Testing](https://github.com/Kennethkcpdhs/Honey_Pancake/blob/master/pythontesting/bankacct/test_bankacct.py)

## Socket Programming
Client and socket

socket.send can send less bytes than requested

socket.sendall sends the entire data or throws an error

```python
#server code
import socket

server_socket = socket.bind(('127.0.0.1',12345))
server_socket.listen()
conn, addr = server_socket.accept()

while some_condition:
    #receive input from client
    msg = conn.recv(1024).decode()
    
    #sendall sends every byte or throws an exception
    conn.sendall(b' Some stuff ')
    conn.sendall(Somestuff.encode()) #alternative encoding
    
conn.close()
server_socket.close()
```

```python
#client code
import socket

client_socket = socket.connect(('127.0.0.1',12345))
client_socket.sendall(b' Some stuff ')
msg = client_socket.recv(1024)
client_socket.close()
```

## Misc Data Conversion
#### Python Dates
```python
import datetime
x = datetime.datetime(2018, 6, 1) #convert to datetime object

#format time into certain string
print(x.strftime("%a"), x.strftime("%B")) 
```
%a --> Wed 	

%A --> Wednesday

%b --> Dec 	

%B --> December

%y 	--> [Year] 18 

%Y 	--> 2018

%x  --> 12/31/18 

%X 	--> 17:41:00
