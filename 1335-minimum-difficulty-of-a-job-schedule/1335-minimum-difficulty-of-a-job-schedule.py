class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:return -1
        if len(jobDifficulty) == d:return sum(jobDifficulty)
        
        @cache
        def dp(ind, dy,_max):
            if ind == len(jobDifficulty): return _max if  not dy else float("inf")
            
            if dy < 0: return float("inf")
            
            _max = max(_max,jobDifficulty[ind])
            ind += 1
            return min(_max+ dp(ind,dy-1,0), dp(ind,dy,_max))
        
        return dp(0,d,0)
        
        