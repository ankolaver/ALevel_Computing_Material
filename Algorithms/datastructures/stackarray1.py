#Array Version
#length cannot be used as it is fixed size from the start

class stackarr:
    max = 10
    def __init__(self):
        #creation of new array
        self.data = []
        for k in range(self.max):
            self.data.append(k)
        self.top = -1 #last item in arr
    
    def empty(self):
        return self.top == -1
    
    def full(self):
        return self.top == self.max-1
    
    def push(self,data): #insert
        if self.full():
            print("Full liao")
            return -1 #continue with other functions
        else: 
            self.top+=1
            self.data[self.top] = data
            #change existing values added to stack
            
    def pop(self):
        if self.empty():
            print("\n Empty liao")
            return -1
        else:
            self.data[self.top] = "Changed"
            self.top-=1 #change index

    def display(self):

        temp = self.top #essential not to change original variable
        while temp>=0:
            print(self.data[temp], end = ' ')
            temp -= 1


#main
s = stackarr()
s.push("Macbook-Pro")
s.push("Lenovo-910")
s.push("HP-Envy-13")
s.pop()
s.push("LG-Gram-13")
s.display()
print("\n",s.data)
