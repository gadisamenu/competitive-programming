class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        j  = 0
        lgth = len(nums)
        
        while j < lgth:
            if nums[j]  != 0:
                if i < j:
                    nums[i] = nums[j]
                    nums[j] = 0
                j += 1
                i += 1
            else:
                j += 1
                
            