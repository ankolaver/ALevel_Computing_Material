#init with array
#empty
#full
#size has been replaced with a simple addition
#enqueue
#dequeue
#peek
#display --> comparing between the front and the rear

'''Using arrays to create the queue'''
class Queue:
    max = 10
    
    def __init__(self):
        self.queue = []
        for k in range(self.max):
            self.queue.append(k)
        self.front = 0 #location for inserting and deleting
        self.rear = 0 
        self.length = 1
    
    def empty(self):
        return self.front == self.rear
    
    def full(self):
        return self.length == self.max-1
    
    def enqueue(self,inputdata):
        if self.full():
            print("Cannot insert, full alrdy")
            return -1
        else:
            self.queue[self.rear] = inputdata
            self.rear +=1
            self.length +=1
    
    def dequeue(self):
        if self.empty():
            print("Cannot remove, empty alrdy")
            return -1
        else:
            data = self.queue[self.front]
            self.front +=1
            self.length -=1
        
    def peek(self):
        return self.queue[self.front]
        #calling first index in the array

    def display(self):
        if self.empty():
            print("Empty queue")

        else:
            curr = self.front #identify last index
            print("Current", curr)
            while curr<self.rear:
                print(self.queue[curr], end = ' ')
                curr+=1

        '''
        else:
            if self.front<self.rear:
                for i in range(self.front,self.rear):
                    print(self.queue[i], end = ' ')
            else: #wrap around to ascending
                for j in range(self.front,self.max):
                    print(self.queue[j], end = ' ')
                for k in range(0, self.rear):
                    print(self.queue[k], end = ' ')'''


# main
q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(7)
q.enqueue(12)
q.enqueue(23)
q.enqueue(56)
q.enqueue(56)
q.enqueue(56)
q.dequeue()
q.dequeue()
q.enqueue(11)
q.enqueue(5)
q.enqueue(99)
q.dequeue()
print(q.queue)
q.display()
