class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0]*(k+1)
        self.start = 0
        self.end = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.data[self.end] = value
        self.end = (self.end + 1)% len(self.data)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.start = (self.start+1)%len(self.data)
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.start]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.end-1]
        
    def isEmpty(self) -> bool:
        return self.end == self.start
        
    def isFull(self) -> bool:
        return (self.end + 1)%len(self.data) == self.start
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()