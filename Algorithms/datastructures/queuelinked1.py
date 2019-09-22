#queue linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def is_empty(self):
        return self.rear == self.front == None
    
    def is_full(self):
        pass # queues cannot become full
    
    #add data in from the back
    def enqueue(self, inputdata):
        node = Node(inputdata)
        #ensure that the "Arbitary' front is completely filled up before going to the back
        if self.is_empty():
            self.front = node 
        else:
            self.rear.link = node
        self.rear = node
        self.length +=1
    
    def dequeue(self):
        if self.is_empty():
            print("Cannot delete from the empty queue")
            return -1 #exit dequeue function immediately
        else:
            removedata = self.front.data = None 
            if self.front.link == None: #last node
                self.front = self.rear = None 
                
            else: #not the last node
                self.front = self.front.link
            self.length-=1
            
    def display(self):
        if self.is_empty():
            print("Empty queue")
        else:
            curr = self.front
            while curr != None:
                print(curr.data, end = '  ')
                curr = curr.link
        print("\ncurr length:",self.length)

#main
q = Queue()
q.enqueue("Mate-30-Pro")
q.enqueue("Galaxy-Note-10")
q.enqueue("Nokia-6.2")
q.enqueue("Mi-A3")
q.dequeue()
q.dequeue()
q.display()  
    
    
