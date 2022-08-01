class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number = 0
        
        for n in nums:
            number ^= n
            
        for n in range(len(nums)+1):
            number ^= n
            
        return number
        