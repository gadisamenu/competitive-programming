class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(words)
        heap = []
        for word in words_count:
                heappush(heap,(-words_count[word],word))
                
        k_frequents = []
        while heap and k:
            k_frequents.append(heappop(heap)[1])
            k-= 1
            
        return k_frequents