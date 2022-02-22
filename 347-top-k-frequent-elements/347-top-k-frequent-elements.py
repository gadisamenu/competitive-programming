import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        values  = list(freq.values())
    
        heapq.heapify(values)
        largest = heapq.nlargest(k,values)
        largest = set(largest)
        ans = []
        for n in largest:
            for k,v in freq.items():
                if v == n:
                    ans.append(k)
        return ans
        
