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
        return self.top == -1
        
    def push(self,value):
        if self.is_full():
            #print("stack full")
            return -1 #continues
        else:
            self.top += 1
            self.data[self.top] = value
    
    def pop(self): #remove
        if self.is_empty():
            #print("stack empty")
            return -1
        
        else:
            self.top -= 1
            return self.data[self.top+1] #leaves variables in there, allows for desired pop
            
        
            
    def display(self):
        for k in range(self.top+1):
            print(self.data[self.top-k], end = '\n')
        #print(self.data)

#main
import sys
import numpy as np
import pandas as pd

checkeqn = stack()
equation = "[(3/5))]"
brackets = [40,41,123,125,91,93]
closing_brack = [93,125,41] #ascii of closing brackets
opening_brack = [40,123,91]
pair1  = [40,41]
pair2 = [91,93]
pair3 = [123,125]

total_brack = 0
for stuff in equation:

    if ord(stuff) in brackets:
        
        if (ord(stuff)) in opening_brack:
            total_brack+=1
            checkeqn.push(stuff)
            
        
        other = checkeqn.pop()
        #print(stuff,other)
        if (ord(stuff) in closing_brack):
            if checkeqn.is_empty():
                output = "No corresponding opening bracket"
                print("No corresponding opening bracket")
                sys.exit()
            #print(ord(stuff),ord(other))
            
            if abs(ord(stuff)-ord(other))>3:
                output = "Pairs of brackets must match"
                print("Pairs of brackets must match")
                sys.exit()

            if (ord(stuff)==ord(other)):
                output = "Pairs of brackets must match"
                print("Pairs of brackets must match")
                sys.exit()
                
    #checkeqn.display()
    
final = checkeqn.pop()
#secondfinal = checkeqn.pop()

if checkeqn.is_empty() == True and total_brack>1:
    output = "Success"
    print("Success")


else: 
    output = "No closing bracket"
    print("No closing bracket")


#can't use sys.exit if running in IDLE
# one opening bracket but no close bracket??
