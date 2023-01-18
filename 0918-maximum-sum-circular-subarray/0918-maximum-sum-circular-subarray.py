class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
     
        _min = 0
        cur_sum = 0
        not_full = False
     
        for i in range(len(nums)):
            cur_sum += nums[i]
            _min = min(_min,cur_sum)
            if cur_sum > 0:
                not_full = True
                cur_sum = 0
        _sum = sum(nums)
        
        
        _max = nums[0]
        for i in range(len(nums)):
            cur_sum += nums[i]
            _max = max(_max,cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        
        return max(_sum - _min,_max) if not_full  else _max
            