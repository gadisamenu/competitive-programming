class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix = {0:-1}
        _sum = 0
        
        for i in range(len(nums)):
            _sum += nums[i]
            m = _sum%k
            if m in prefix:
                if i - prefix[m] > 1:
                    return True
            else:
                prefix[m] = i
        return False