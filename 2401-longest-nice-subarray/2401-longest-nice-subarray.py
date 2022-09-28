class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        _sum = 0
        ans = 0
        i = 0
        j = 0
        
        while j < len(nums):
            while _sum & nums[j] != 0:
                _sum ^= nums[i]
                i += 1
            _sum |= nums[j]
            ans = max(ans,j-i+1)
            j += 1
        return ans
            