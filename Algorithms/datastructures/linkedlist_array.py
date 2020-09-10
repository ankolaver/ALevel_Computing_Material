class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedStructure:
    store = [Node('') for i in range(11)]
    def __init__(self):
        self.Head = 0
        self.Tail = 0
        self.Free = 1
        self.length = 0
        
    def is_empty(self):
        return self.length == 0
    
    def is_full(self):
        return self.length == 10
    
    def add(self, newdata):
        if self.is_full():
            return "Full, unable to insert"
        else:
            index = self.Free
            
            #assign iterator
            curr = self.Head
            prev = 0
            
            while curr != 0 and newdata > self.store[curr].data:
                #set prev node to current iterator
                prev = curr
                curr = self.store[curr].next

            newnode = Node(newdata)
            
            #add item to list
            self.store[self.Free] = newnode
            self.length+=1
            self.Free+=1
                
            #First node
            if prev == 0:
                self.Head = index
            else:
                #adjust previous pointer
                self.store[prev].next = index
            
            
            #assign newnode pointer to next pointer
            if curr is not None:
                newnode.next = curr
            
            #change tail pointer
            if curr == 0:
                self.Tail = curr
            

            
    def Remove(self,item):
        if self.is_empty():
            return "Empty, unable to remove"
        else:
            curr = self.Head
            prev = 0
            while curr!=0 and self.store[curr].data != item:
                prev = curr
                curr = self.store[curr].next
            forward = self.store[curr].next
            print(curr)
            
            #adjust back pointer
            if forward is not None:
                self.store[prev].next = forward
            else: #last node
                self.Tail = prev
            
            #remove node
            self.store[curr] = Node('')
            self.Free = curr
            
        
    def display(self):
        curr = self.Head
        while curr!=0 and curr != self.Tail:
            print(self.store[curr].data,str(self.store[curr].next), curr)
            curr = self.store[curr].next
        #print(self.store[curr].data,str(self.store[curr].next),curr)

            
    def PrintStructure(self):
        print("Head: {0:<3} Tail:{1:<3} Length:{2:<3}".format(self.Head,self.Tail,self.length))
        for item in self.store:
            if item != "":
                print(item.data, item.next, end=" || ")
        print()
    
    
    

    
animals = LinkedStructure()

animals.add("Dog")
animals.add("Bat")
animals.add("Wildebeest")
animals.add("Toad")
animals.add("Horse")
animals.add("Zebra")
animals.add("Cheetah")
animals.add("Yelp")
animals.display()
animals.PrintStructure()
animals.Remove("Toad")
animals.display()
animals.PrintStructure()
animals.Remove("Zebra")
animals.display()
animals.PrintStructure()
animals.add("Tiger")
animals.display()
animals.PrintStructure()

    
