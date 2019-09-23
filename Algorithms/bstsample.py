# BST class

class BST:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if data < self.data: # insert to left
            if self.left is None: # insert as left leaf
                self.left = BST(data)
            else: # insert to left subtree
                self.left.insert(data)
        else: # insert to right
            if self.right is None: # insert as right leaf
                self.right = BST(data)
            else:
                self.right.insert(data)

    def search(self, target):
        if self.data == target: # terminating case
            return "Found"
        elif self.left is None and self.right is None: # not found 
            return "Not found" # terminating case
        elif target < self.data: # search left
            if self.left is None:
                return "Not found"
            else: # continue left search
                return self.left.search(target) # recursive case
        else: # target > self.data, so search right
            if self.right is None:
                return "Not found"
            else: # continue right search
                return self.right.search(target) # recursive case
       
    def lookup(self, data, parent=None):
        if self.data == data: # found
            return self, parent
        elif data < self.data: # go left
            if self.data is None:
                return None, None
            else:
                return self.left.lookup(data, self)
        else: # go right
            if self.data is None:
                return None, None
            else:
                return self.right.lookup(data, self)

    def delete(self, data):
        # get to be deleted node and its parent
        node, parent = self.lookup(data)
        if node is not None:
            if (node.left is None) and (node.right is None): # case 1: 0 child
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            elif (node.left is None) != (node.right is None): # case 2: 1 child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else: # case 3: 2 children
                # replace with inorder successor
                parent = node
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.data = successor.data
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
        else:
            return "Not found"
    
    def minimum(self):
        if self.left is None:
            print("Smallest:", self.data)
        else:
            return self.left.minimum()
    
    def maximum(self):
        if self.right is None:
            return self.data
        else:
            return self.right.maximum() 
            
    def inorder(self):
        if self.left: # if self.left is not None:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right: # if self.right is not None:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=' ')
        if self.left: # if self.left is not None:
            self.left.preorder()
        if self.right: # if self.right is not None:
            self.right.preorder()            

    def postorder(self):
        if self.left: # if self.left is not None:
            self.left.postorder()
        if self.right: # if self.right is not None:
            self.right.postorder()
        print(self.data, end=' ')

    def reverse(self):
        if self.right: # if self.right is not None:
            self.right.reverse()
        print(self.data, end=' ')           
        if self.left: # if self.left is not None:
            self.left.reverse()
     
  
# main
bst = BST(50)
bst.insert(30)
bst.insert(80)
bst.insert(10)
bst.insert(40)
bst.insert(70)
bst.insert(90)
bst.inorder()
print()
bst.delete(90) # 0 child
bst.delete(70) # 1 child
bst.delete(50) # 2 children
bst.inorder()
print()
#bst.preorder()
#print()
#bst.postorder()
#print()
#bst.reverse()
#print()
#print(bst.search(80))
#print(bst.search(100))
#print(bst.minimum())
#print(bst.maximum())
