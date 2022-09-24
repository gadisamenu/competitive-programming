class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]  <= nums[-1]:return nums[0]
        
        left_v = nums[0]
        right_v = nums[-1]
        left = 0
        right = len(nums)-1
    
        while left < right:
            md = left + (right-left)//2
            
            if nums[md] <= right_v and nums[md] <= left_v:
                right = md
            elif nums[md] >= right_v and nums[md] >= left_v:
                left =md +1

        
        return nums[left]