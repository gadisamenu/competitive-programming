class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:                
        if len(self.max_heap) > len(self.min_heap):
            if -self.max_heap[0] > num:
                num = -heapreplace(self.max_heap,-num)
            heappush(self.min_heap,num)
        else:
            if self.min_heap and self.min_heap[0] < num:
                num = heapreplace(self.min_heap,num)
            heappush(self.max_heap,-num)
        
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2
        return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()