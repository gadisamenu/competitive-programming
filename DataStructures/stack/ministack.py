class MinStack:

    def __init__(self):
        self.value = []
        
    def push(self, val: int) -> None:
        self.value.append(val)
    def pop(self) -> None:      
        return self.value.pop()

    def top(self) -> int:
        return self.value[-1]
    def getMin(self) -> int:
        return min(self.value)      


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()