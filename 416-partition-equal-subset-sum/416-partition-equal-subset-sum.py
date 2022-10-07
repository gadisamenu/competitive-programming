class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 == 1:return False
        _sum //= 2
                
        @cache
        def dp(ind,sm):
            if sm == _sum: return True
            if ind >= len(nums): return False
            return dp(ind+1, sm + nums[ind]) or dp(ind+1,sm)
            
        return dp(0,0)
                
            