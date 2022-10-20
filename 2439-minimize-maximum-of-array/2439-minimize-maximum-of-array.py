class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        _sum = nums[0]
        
        for i in range(1,len(nums)):
            _sum += nums[i]
            if ans < nums[i]:
                ans = max(ans,_sum/(i+1))
        return ceil(ans)
                