import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            if not self.maxHeap and not self.minHeap:
                heapq.heappush(self.maxHeap,-num)
            else:
                if -self.maxHeap[0] > num:
                    heapq.heappush(self.maxHeap,-num)
                else:
                    heapq.heappush(self.minHeap,num)
                    
        elif len(self.maxHeap) > len(self.minHeap):
            if -self.maxHeap[0] > num:
                heapq.heappush(self.minHeap,-heapq.heapreplace(self.maxHeap,-num))
            else:
                heapq.heappush(self.minHeap,num)
        else:
            if self.minHeap[0] < num:
                heapq.heappush(self.maxHeap,-heapq.heapreplace(self.minHeap,num))
            else:
                heapq.heappush(self.maxHeap,-num)
                
            
        
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0]+ self.minHeap[0])/2
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return self.minHeap[0]
        
        
        

        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()