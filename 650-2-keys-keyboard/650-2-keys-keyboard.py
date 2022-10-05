class Solution:
    def minSteps(self, n: int) -> int:
        
        
        @cache
        def dp(cur,coppied):
            if cur + coppied > n:
                return float("inf")
            if cur == n:return 0
            if cur + coppied  == n: return 1
            if coppied:
                return 1+ min(dp(cur+coppied,0),dp(cur+coppied,coppied))
            
            return 1+ dp(cur,cur)
        
        return dp(1,0)
            
        
    