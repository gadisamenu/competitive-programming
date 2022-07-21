class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(key=lambda x:-x)
        lgth = len(citations)
        
        max_h_index = 0
        for n in range(lgth):
            index = min(n+1,citations[n])
            max_h_index = max(max_h_index,index)
                
        return max_h_index
                
                
        