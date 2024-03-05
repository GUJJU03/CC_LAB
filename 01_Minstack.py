class Minstack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stack=[]
        self.min_stack=[]

    def is_empty(self):
        return len(self.stack)==0
    def is_full(self):
        return len(self.stack)==self.capacity
    
    def push(self,item):
        if self.is_full():
            print("overflow")
        else:
            self.stack.append(item)
            if len(self.min_stack) == 0 or item < self.min_stack[-1]:
                self.min_stack.append(item)
            print(self.min_stack)

    def pop(self):
        if self.is_empty():
            print("underflow")
        else:
            if(self.min_stack[-1]==self.stack[-1]):
                self.min_stack.pop()
            self.stack.pop()
            print(self.stack)      

    def top(self):
        if self.is_empty():
            print("underflow")
        else:
            print("Top Element :",self.stack[-1])

    def get_min(self):
        if self.is_empty():
            print("underflow")
        else:
            print("Min Element :",self.min_stack[-1])

obj=Minstack(5)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
obj.top()
obj.get_min()
                                      