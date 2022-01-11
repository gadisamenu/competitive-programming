class MyCircularDeque:

    def __init__(self, k: int):
        self.values = [0] *(k+1)    
        self.head = 0
        self.end = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.head == 0:
            self.head = len(self.values)-1
        else:
            self.head = self.head -1
            
        self.values[self.head] = value
        
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.values[self.end] = value
        
        if self.end == len(self.values) -1:
            self.end = 0
        else:
            self.end += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == len(self.values)-1:
            self.head = 0
        else:
            self.head = self.head +1
            
        return True    

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.end == 0:
            self.end = len(self.values) -1
        else:
            self.end = self.end -1
        return True
    
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.values[self.head]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.values[self.end-1]

    def isEmpty(self) -> bool:
        if self.end == self.head:
            return True
        
    def isFull(self) -> bool:
        if self.end > self.head:
            if self.end - self.head == len(self.values) -1:
                return True
        if self.end + 1 == self.head:
            return True
            
            
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()