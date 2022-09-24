class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = -float("inf")
        cur = 0
        
        for n in nums:
            cur += n
            if cur > _max:
                _max = cur
            if cur < 0 : cur = 0
                
        return _max
        
