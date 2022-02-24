import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        fre =Counter(words)
        
        heap = []
        result = []
        for ke,va in fre.items():
            heapq.heappush(heap,(-va,ke))
        
        while heap and k:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result