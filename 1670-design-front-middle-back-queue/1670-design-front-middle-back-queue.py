class FrontMiddleBackQueue:

    def __init__(self):
        self.fst_half = deque()
        self.snd_half = deque()

    def pushFront(self, val: int) -> None:
        if len(self.fst_half) > len(self.snd_half):
            self.snd_half.appendleft(self.fst_half.pop())
        self.fst_half.appendleft(val)
        
    def pushMiddle(self, val: int) -> None:
        if len(self.fst_half) > len(self.snd_half):
            self.snd_half.appendleft(self.fst_half.pop())
        self.fst_half.append(val)
       

    def pushBack(self, val: int) -> None:
        if len(self.snd_half) > len(self.fst_half):
            self.fst_half.append(self.snd_half.popleft())
        self.snd_half.append(val)
     

    def popFront(self) -> int:
        if not self.snd_half and not self.fst_half: return -1
        if len(self.snd_half) > len(self.fst_half):
            self.fst_half.append(self.snd_half.popleft())
   
        return self.fst_half.popleft()
        
    
    def popMiddle(self) -> int:
        if not self.snd_half and not self.fst_half: return -1
        if len(self.snd_half) > len(self.fst_half):
            return self.snd_half.popleft()

        return self.fst_half.pop()
    
    def popBack(self) -> int:
        if not self.snd_half and not self.fst_half: return -1
        if len(self.snd_half) < len(self.fst_half):
            self.snd_half.appendleft(self.fst_half.pop())
       
        return self.snd_half.pop()
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()