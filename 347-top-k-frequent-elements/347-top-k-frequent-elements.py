import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter (nums)
        kTop =[]
        for ke,v in freq.items():
            if len(kTop) < k:
                heapq.heappush(kTop,(v,ke))
            else:
                heapq.heappushpop(kTop,(v,ke))
        ans=[]
        print(kTop)
        for value,key in kTop:
            ans.append(key)
        return ans
        
