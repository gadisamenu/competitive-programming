class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
             
        @cache
        def dp(nth,tgt):
            if tgt < 0:return 0
            if nth > n:
                if tgt == 0: return 1
                return 0
            ans = 0
            for i in range(1,k+1):
                ans += dp(nth+1,tgt-i)
                
            return ans

            
        
        return dp(1,target)%1000000007
        
