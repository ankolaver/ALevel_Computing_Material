#no search added yet
class Node:
    def __init__(self, data=0):
        self.data = data
        self.link = None
    
    def get_data(self):
        return self.data
    
    def get_link(self):
        return self.link
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_link(self, new_link):
        self.link = new_link

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add(self,value):
        temp = Node(value)
        temp.set_link(self.head)
        self.head = temp
        self.length +=1
    
    def update(self,target,new_value):
        curr = self.head
        found = False
        while curr!=None and not found:
            if curr.get_data()==target:
                found = True
                curr.set_data(new_value)
            else:
                curr = curr.get_link()
        if found:
            print("Updated")
        else:
            print("Error Updating")
    
    def delete(self,target):
        prev = self.head
        curr = self.head
        found = False
        while curr!=None and not found:
            if curr.get_data() == target:
                found = True
                prev.set_link(curr.get_link())
            else:
                prev = curr
                curr = curr.get_link
        #error messages
        if found: 
            print("Deleted")
            self.length-=1
        else:
            print("error deletng")
    
    def display(self):
        curr = self.head
        while curr!=None:
            print(curr.data,end=' ')
            curr = curr.get_link()
        print("\nlength:", self.length)
#main
linkedlist = LinkedList()
linkedlist.add(34)
#print(linkedlist.head.data)
#print(linkedlist.head.link)
linkedlist.add(5)
linkedlist.add(99)
linkedlist.display()
                
