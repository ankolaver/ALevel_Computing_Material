class Node:
    def __init__(self,Data,Priority):
        self.Data = str(Data)
        self.Priority = Priority
        self.Pointer = None

class PQueue:
    def __init__(self):
        self.Front = self.Rear = None
        self.length = 0

    # checks if queue is empty
    def isempty(self):
        return self.Front == None

    def JoinPQueue(self,NewItem,Priority):
        newnode = Node(NewItem,Priority)
        self.length+=1
        
        #empty queue
        if not self.Rear:
            self.Front = self.Rear = newnode
            return
        
        #check with front node
        if self.Front.Priority < newnode.Priority:
            newnode.Pointer = self.Front
            self.Front = newnode
            return
        
        prev = None
        curr = self.Front
        
        #traverse queue
        while(curr and newnode.Priority <= curr.Priority):
            prev = curr
            curr = curr.Pointer
            
        #insert at the middle of queue
        if curr and prev:
            #readjust prev pointer to new node
            prev.Pointer = newnode
            #newnode Pointer = curr
            newnode.Pointer = curr
            
        else: #insert at the end 
            self.Rear.Pointer = newnode
            self.Rear = newnode
    
    def LeavePQueue(self):
        if self.isempty(): return "Cannot delete from the empty queue"
        else:
            leave = self.Front
            self.Front = self.Front.Pointer
            if self.Front == None: self.Rear = None
            return "Deleted Successfully"
        
    def OutputQueue(self):
        if self.isempty(): return "No Priority Queue to show"
        else:
            curr = self.Front
            print("{0:<10}{1:<10}".format("Name","Priority"))
            while curr != None:
                print("{0:<10}{1:<10}".format(curr.Data,curr.Priority))
                curr = curr.Pointer
        
            print("\nCurr Number of Patients:",self.length)
    
#main
patients = PQueue()
patients.JoinPQueue("John",2)
patients.JoinPQueue("Duh",1)
patients.JoinPQueue("Pat",2)
patients.OutputQueue()
patients.LeavePQueue()
patients.OutputQueue()
