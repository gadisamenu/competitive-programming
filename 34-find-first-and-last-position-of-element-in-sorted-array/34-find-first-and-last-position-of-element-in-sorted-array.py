class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.search(nums,target),self.search(nums,target,False)]
        
    
    
    
    def search(self,nums,target,first = True):
        
        left = 0
        right = len(nums) -1
        best = -1
        
        while left <= right:
            
            m = left + (right-left)//2
            
            if nums[m] == target:
                best = m
                if first:
                    right =m-1
                else:
                    left = m+1
            elif nums[m] > target:
                right = m-1
            elif nums[m] < target:
                left = m+ 1
            
        return best