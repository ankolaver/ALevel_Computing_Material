class TreeNode:
    def __init__(self,Value):
        self.Value = Value
        self.Left = None
        self.Right = None


class BSTree:
    def __init__(self):
        self.Root = None
        self.Count = 0
        
    def Insert(self,newvalue):
        newnode = TreeNode(newvalue)
        if self.Root is None:
            self.Root = newnode
        else:
            current = self.Root
            Found = False
            while not Found:
                if newnode.Value < current.Value:
                    if current.Left is None:
                        current.Left = newnode
                        self.Count+=1
                        Found = True
                    else:
                        current = current.Left
 
                else: # newnode >= current.Value 
                    if current.Right is None:
                        current.Right = newnode
                        self.Count+=1
                        Found = True
                    else: 
                        current = current.Right
    
    def ReverseOrder(self, item):
        if item is not None:
            self.ReverseOrder(item.Right)
            print(item.Value, end=" ")
            self.ReverseOrder(item.Left)
                
    def Search(self,value,node = None):
        if not node:
            node = self.Root
        if node.Value == value:
            return "Found value"
        else:
            if value >= node.Value:
                if node.Right:
                    return self.Search(value,node.Right)
            else:
                if node.Left:
                    return self.Search(value,node.Left)
        return "Unable to find value"
        
    def Count(self):
        return self.Count
        
        
newtree = BSTree()

with open('INSERTTOTREE.txt') as f:
    names = f.readlines()
    for name in names:
        name = name.strip()
        newtree.Insert(name)
        
newtree.ReverseOrder(newtree.Root)
newtree.Search("John")
