import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq  = Counter(s)
        heaped =[]
        
        for k,v in freq.items():
            heapq.heappush(heaped,(-v,k))
            
        ans = []
        for i in range(len(freq)):
            popped = heapq.heappop(heaped)
            
            ans.append(popped[1]*(-popped[0]))
            
        return "".join(ans)
        
        