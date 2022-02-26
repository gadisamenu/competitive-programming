import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x,stones))
        
        heapq.heapify(stones)
        while len(stones)>1:
            x = -heapq.heappop(stones)
            y = - stones[0]
            if x == y:
                heapq.heappop(stones)
            else:
                heapq.heapreplace(stones,-(x-y))
            print(stones)
            
            
        if stones:
            return -stones[0]
        return 0
                