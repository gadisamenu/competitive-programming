class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sm = nums[0]
        _min = float('inf')
        i = 0
        j = 0
        while j < len(nums):
            while sm >= target:
                _min = min(_min,j-i+1)
                sm -= nums[i]
                i += 1
                
            j += 1  
            if j < len(nums):  
                sm += nums[j]
        
        return 0 if _min == float("inf") else _min
            