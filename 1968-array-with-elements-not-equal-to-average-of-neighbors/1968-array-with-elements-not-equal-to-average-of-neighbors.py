class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 1
        while i+1 < len(nums):
            nums[i],nums[i+1] = nums[i+1],nums[i]
            i+=2
        return nums
            
        
        