class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix_sum = {0:-1}
        _sum = 0
        
        for i in range(len(nums)):
            _sum += nums[i]
            remainder = _sum%k
            if remainder in prefix_sum:
                if i - prefix_sum[remainder] > 1:
                    
                    return True
            else:
                prefix_sum[remainder] = i
        return False