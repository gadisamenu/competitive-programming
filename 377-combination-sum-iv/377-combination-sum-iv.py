class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(sm:int)->int:
            if sm  > target:
                return 0
            if sm == target:
                return 1
            
            ans = 0
            for n in nums:
                ans +=  dp(sm + n)
            return ans
            
        return dp(0)
                
        