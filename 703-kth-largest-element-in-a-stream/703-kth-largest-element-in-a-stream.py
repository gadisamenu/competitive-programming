import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        num = heapq.nlargest(self.k,nums)      
        heapq.heapify(num)
        self.heaped =num
        
    def add(self, val: int) -> int:
        if len(self.heaped) < self.k:
            heapq.heappush(self.heaped,val)
        else:
            heapq.heappushpop(self.heaped,val)
        return self.heaped[0]
       
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)