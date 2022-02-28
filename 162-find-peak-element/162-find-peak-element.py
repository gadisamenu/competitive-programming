class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        
        left= 0 
        right = len(nums) -1
        
        while left <= right:
            
            m  = left + (right -left)//2
            
            if m == 0:
                if nums[m] > nums[m+1]:
                    return m
                else:
                    left = m+1
            elif m == len(nums)-1:
                if nums[m] > nums[m-1]:
                    return m
                else:
                    right = m-1
                
            else:
                if nums[m] > nums[m-1]   and nums[m+1] < nums[m]:
                    return m

                elif nums[m] < nums[m-1]:
                    right = m-1

                elif nums[m] < nums[m+1]:
                    left = m+1
        
                