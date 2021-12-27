class MyQueue:

    def __init__(self):
        self.value = []
    def push(self, x: int) -> None:
        self.value.append(x)
    def pop(self) -> int:
        popped = self.value[0]
        self.value = self.value[1:]
        print(self.value)
        return popped
    def peek(self) -> int:
        peeked = self.value[0]
        return peeked
    def empty(self) -> bool:
        if self.value:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()