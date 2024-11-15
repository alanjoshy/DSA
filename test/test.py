class hashtable:
    def __init__(self, size = 10):
        self.size = size 
        self.table = [[] for _ in range(self.size)] 
        
    def aschihash(self,key):
        ascihash = sum(ord(char) for char in key) 
        return (ascihash % self.size)
    
    def insert(self,key,value):
        index = self.aschihash(key) 
        bucket = self.table[index] 
        
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value) 
                print(f"updated : {key} --> {value}") 
                return 
        bucket.append((key,value)) 
        print(f"inserted: {key} --> {value}") 
        
    def view(self,key):
        index = self.aschihash(key) 
        bucket = self.table[index] 
        
        for (k,v) in bucket:
            if k == key:
                return v   
            else:
                print(f"{key} is not found") 
                
    def delete(self,key):
        index = self.aschihash(key)         
        bucket = self.table[index] 
        
        for i,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i] 
                print(f"deleted .... {i}") 
            else:
                print(f"{key} is not found" ) 
                
    def display(self):
        for i,bucket  in enumerate(self.table):
            if bucket:
                print(f"bucket{i} : {bucket}")
            else:
                print(f"bucket {i} : empty")
            
hsh = hashtable() 
hsh.insert("banana",10) 
hsh.insert("apple",50) 
hsh.display()
            