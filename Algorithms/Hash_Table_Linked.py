#Array Implementation adapted from RVHS 2019 Paper
class linkedlist:
    
    def __init__(self,size):
        self.size = size
        self.head = -1 #changes with the new insert
        self.nextFree = 0
        self.keys = [-1 for i in range(size)] #store hash key for retrieval later
        self.datas = ["None" for i in range(size)]
        self.ptrs = [(-1) for i in range(size)]
        for i in range(1, size):
            self.ptrs[i-1] = i
        
    def insert(self,key,value):
        if self.nextFree == -1:
            print("Full liao")
            return
        else:
            #current free slot
            currslot = self.nextFree
            
            #set new free before occupied
            self.nextFree = self.ptrs[currslot]
            
            #assign values
            self.keys[currslot] = key
            self.datas[currslot] = value
            self.ptrs[currslot] = self.head
            print(f"{key} {value} Curr Head {self.head}")
            #set self.head
            self.head = currslot

    def search_by_key(self, key):
        if self.head == -1:
            return "Not here"
        else:
            curr = self.head
            while curr!=-1:
                if self.keys[curr] == key:
                    return self.datas[curr]
                curr = self.ptrs[curr]
    
    def displayList(self):       
        if self.head != -1:
            curr =  self.head
            
            while curr != -1:
                print(self.datas[curr],self.ptrs[curr], end="|")
                curr =  self.ptrs[curr]
            
            print("\n\nKeys:",self.keys)
            print("Ptrs:",self.ptrs)
            print("Datas:",self.datas)
                
class Hashtable:
    def __init__(self, ht_size, ll_size):
        self.table = []
        self.ht_size = ht_size
        for i in range(ht_size):
            self.table.append(linkedlist(ll_size))
            
    def hash_func(self,key):
        return key%self.ht_size
    
    def search(self,key):
        return self.table[self.hash_func(key)].search_by_key(key)
        
    def insert_kv_pair(self,key,newvalue):
        hash_v = self.hash_func(key)
        self.table[hash_v].insert(key,newvalue)
        
    def display_ht(self):
        for item in self.table:
            #print(item)
            print(item.displayList())

        
ht = Hashtable(11,10)
ht.insert_kv_pair(10,"apple")
ht.insert_kv_pair(6,"banana")
ht.insert_kv_pair(32,"carrot")
ht.insert_kv_pair(93,"dragonfruit")
ht.insert_kv_pair(34,"eggplant")
ht.insert_kv_pair(65,"figs")
print(ht.search(93))
print(ht.search(6))
ht.display_ht()
