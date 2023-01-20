class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
     
        pairs.sort(key=lambda x:(x[1],-x[0]))
        bound = pairs[0][1]
        lgth = 1
        
        for i in range(1,len(pairs)):
            if bound < pairs[i][0]:
                bound = pairs[i][1]
                lgth +=1 
                
        return lgth
