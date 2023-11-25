class Queue :
    
    def __init__(self) :
        self.queue = []
        
    def enqueue(self, X) :
        self.queue.append(X)
        
    def dequeue(self) :
        return None if self.empty() else self.queue.pop(0)
    ßß
    def peek(self) :
        return None if self.empty() else self.queue[0]
    
    def size(self) :
        return len(self.queue)
    
    def empty(self) :
        return len(self.queue) == 0
    