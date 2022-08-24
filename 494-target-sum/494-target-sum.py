class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
  
        @cache
        def dp(index,sm):
            if index == len(nums):
                return 1 if sm == target else 0
            return  dp(index+1 ,sm+nums[index]) + dp(index+1, sm-nums[index])
        return dp(0,0)