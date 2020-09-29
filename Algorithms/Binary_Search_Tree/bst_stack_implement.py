class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
        self.count = 0
        
    def insert_iterative(self, newdata):
        if self.root is None:
            self.root = Node(newdata)
        else:
            found = False
            curr = self.root
            while not found:
                if newdata<curr.data: #go right
                    if curr.left is None:
                        curr.left = Node(newdata)
                        found = True
                    else:
                        curr = curr.left
                else: #newdata >=curr.value
                    if curr.right is None:
                        curr.right = Node(newdata)
                        found = True
                    else:
                        curr = curr.right
                        
    def insert_recursive(self, root,newdata):
        if newdata < root.data:
            if root.left is None:
                root.left = Node(newdata)
            else:
                self.insert_recursive(root.left,newdata)
        else:
            if root.right is None:
                root.right = Node(newdata)
            else:
                self.insert_recursive(root.right,newdata)
        
            
    def inorder(self,root):
        curr = root
        stack = []
        done = False
        while not done:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                print(curr.data, end=" ")
                curr = curr.right
            else:
                done=True
    
    def postorder(self,root):
        curr = root
        li = []
        done = False
        print()
        while not done:
            if curr is not None:
                li.append(curr)
                curr = curr.right
            elif li:
                curr = li.pop()
                print(curr.data, end=" ")
                curr = curr.left
            else:
                done = True
                
    def preorder(self,root):
        curr = root
        li = []
        print()
        li.append(curr)
        while li:
            curr = li.pop()
            print(curr.data, end=" ")
            if curr.left:
                li.append(curr.left)
            if curr.right:
                li.append(curr.right)
            
    
t = Tree()
t.insert_iterative(6)
t.insert_iterative(7)
t.insert_iterative(1)
t.insert_iterative(2)
t.insert_recursive(t.root,8)
t.insert_recursive(t.root,18)
t.inorder(t.root)
t.preorder(t.root) 
t.postorder(t.root)

'''
1 2 6 7 8 18 
6 7 8 18 1 2 
18 8 7 6 2 1 
'''
