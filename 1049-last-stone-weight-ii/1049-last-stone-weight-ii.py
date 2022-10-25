class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        lgth = len(stones)
        
        @cache
        def dp(i,_sum):
            if i >= lgth:return _sum
            answer=  min(dp(i+1,abs(_sum - stones[i])),dp(i+1,abs(_sum+stones[i])))
            return answer
        
        return dp(0,0)
        
        
        
                
                