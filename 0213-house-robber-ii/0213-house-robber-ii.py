class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:return nums[0]
        @cache
        def dp(i,last):
            if i >= last:
                return 0
            return max(dp(i+1,last),nums[i]+ dp(i+2,last))    
                
        answer = max(dp(0,len(nums)-1),dp(1,len(nums)))
        return answer
        