class Solution:
    def rob(self, nums: List[int]) -> int:
        lgth = len(nums)
        if lgth == 1:
            return nums[0]
        
        @lru_cache(None)
        def nexts(idx):
            nonlocal lgth
            if idx == lgth-1:
                return nums[idx]
            left = nexts(idx+2) if idx+2 < lgth else 0
            right = nexts(idx+3) if idx+3 < lgth else 0
            
            return left +nums[idx] if left > right else right+nums[idx]
        
        return max(nexts(0),nexts(1))
            
            