class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(ind):            
            if ind == 0:
                return 1
            
            ans = 1
            for n in range(ind-1,-1,-1):
                if nums[ind] > nums[n]:
                    ans = max(ans,dp(n)+1)
            return ans
        
        ans = 0
        for n in range(len(nums)):
            ans = max(ans,dp(n))
            
        return ans
                
            