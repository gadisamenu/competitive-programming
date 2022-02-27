import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lgth = len(score)
        rank  =[0]*lgth
        heaped =[]
        
        for i in range(lgth):
            heapq.heappush(heaped,(-score[i],i))
                       
        rng = min(lgth,3)
                       
        for i in range(rng):
            if i == 0:
                rank[heapq.heappop(heaped)[1]] = "Gold Medal"
            elif i == 1:
                rank[heapq.heappop(heaped)[1]] = "Silver Medal"
            else:
                rank[heapq.heappop(heaped)[1]] = "Bronze Medal"
        i = 4     
        while heaped:
            rank[heapq.heappop(heaped)[1]] = str(i)
            i+=1
        return rank
            
        
        