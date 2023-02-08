class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(ind):
            if ind >= len(nums)-1:
                return 0
            resp = float("inf")
            
            for n in range(1,min(nums[ind]+1,len(nums))):
                if n + ind < len(nums):
                    resp = min(resp,dp(ind+n))
                
            return 1 + resp
        
        return dp(0)
                