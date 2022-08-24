class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(index,sm):
            if index == len(nums):
                return 1 if sm == target else 0
            ret = 0
            ret += dp(index+1 ,sm+nums[index])
            ret += dp(index+1, sm-nums[index])
            return ret
            
        return dp(0,0)