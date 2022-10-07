class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 == 1:return False
        _sum //= 2
        
        dp = [ False for i in range(_sum+1)]
        dp[0] = True
        
        for n in nums:
            for i in range(len(dp)-1,-1,-1):
                if dp[i]:
                    if i + n <= _sum: dp[i+n] = True
        return dp[-1]
                    
            
                
#         @cache
#         def dp(ind,sm):
#             if sm == _sum: return True
#             if sm > _sum: return False
#             if ind >= len(nums): return False
#             return dp(ind+1, sm + nums[ind]) or dp(ind+1,sm)
            
#         return dp(0,0)


                
            