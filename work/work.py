# # push,pop,display stack

class stack:
    def __init__(self):
        self.stack=[] 
        
    def push(self,item):
        self.stack.append(item)
        print(f"element pushed {item}") 
        
    def pop(self):
        if len(self.stack) < 1:
            print("stack is empty")
            return
        self.stack.pop() 
        print("element poped out") 
        
        
    def display(self):
        for i in range(len(self.stack)-1,0,-1):
            print(self.stack[i])  
            print("^ ")
            print("|") 
        
st = stack()
st.push(1)
st.push(2)
st.push(3)
st.display()
st.pop()
st.display() 


