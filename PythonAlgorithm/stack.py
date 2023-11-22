class Stack :
    def __init__(self) :
        self.stack = []
    
    def push(self, X) :
        self.stack.append(X)
        
    def pop(self) :
        return None if self.empty() else self.stack.pop()
    
    def peek(self) :
        return None if self.empty() else self.stack[-1]
    
    def size(self) :
        return len(self.stack)
    
    def empty(self) :
        return len(self.stack) == 0