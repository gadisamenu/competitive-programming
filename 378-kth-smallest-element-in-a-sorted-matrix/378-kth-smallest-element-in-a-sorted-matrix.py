import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lined = []
        
        for row in matrix:
            for col in row:
                heapq.heappush(lined,col)
        
        while k-1:
            heapq.heappop(lined)
            k-=1
            
        return heapq.heappop(lined)