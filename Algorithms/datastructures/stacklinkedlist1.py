class Node:
    def __init__(self, data):
		self.data = data
		self.prev = None
        #previous data

class stack:
	def __init__(self):
		self.top = None
	
	def empty(self):
		return self.top==None
	
	def full(self):
		#not possible
		pass
	
	def push(self, inputdata):
		if self.full(): #not possible
			return -1
		else:
			newnode = Node(inputdata)
            #adding previous item to the next connection
			newnode.prev = self.top
			self.top = newnode
		
	def pop(self):
		if self.empty():
			print("stack empty alrdy")
			return -1
		else:
			deletedata = self.top
			self.top = self.top.prev
			deletedata = None
	
	def display(self):
		curr = self.top
		
		while curr is not None:
			print(curr.data, end=' ')
			curr = curr.prev
		
#main	
s = stack()
s.push("Surfacepro")
s.push("Surfacego")
s.push("Swift5")
s.push("Lunar14")
s.push("x1-carbon")
s.pop()
s.display()
