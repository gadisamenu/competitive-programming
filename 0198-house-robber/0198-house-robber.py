class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(index):
            if index >= len(nums):
                return 0
            return max(dp(index+1),dp(index+2)+nums[index])
        return dp(0)