class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        nums.sort()
        answer = float("inf")
        i = 0 
        j = len(nums)-4
        while j < len(nums):
            answer = min(answer,nums[j]- nums[i])
            i += 1
            j += 1
        
        return answer
        
        