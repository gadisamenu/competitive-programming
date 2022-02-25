class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left =0
        right = len(nums)-1
        
        while left <= right:
            m = left + (right-left)//2
            if nums[m] < target:
                left = m+ 1
            elif nums[m] > target:
                right = m-1
            else:
                return m
        if nums[m] < target:
            return m +1
        return m
        
        