class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        
        @cache
        def dfs(left, right):
            if left >= right:
                return 0
            
            ret = 0
            
            for last in range(left + 1, right):
                prod = nums[left] * nums[last] * nums[right]
                ret = max(ret, prod + dfs(left, last) + dfs(last, right))
            
            return ret
         
        return dfs(0, len(nums) - 1)