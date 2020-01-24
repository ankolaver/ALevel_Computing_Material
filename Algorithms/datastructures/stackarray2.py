class stack:
    max = 20
    
    def __init__(self):
        self.data = []
        for k in range(self.max): #creation of new array
            self.data.append(k)
        self.top = -1 #starts from back of array
    
    def is_full(self):
        #automatically shows false or true
        return self.top == self.max-1
    
    def is_empty(self):
        return self.top == 0
        
    def push(self,value):
        if self.is_full():
            print("stack full")
            return -1 #continues
        else:
            self.top += 1
            self.data[self.top] = value
    
    def pop(self): #remove
        if self.is_empty():
            print("stack empty")
            return -1
        
        else:
            self.data[self.top] = None
            self.top -= 1
            
    def display(self):
        for k in range(self.top+1):
            print(self.data[self.top-k], end = '\n')

cars = stack()
cars.push('Toyota Corolla')
cars.push('Lexus LFA')
cars.push('BMW 3')
cars.push('Mercedes A')
cars.display()
