class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum =0
        rightSum =0
        
        for ind in range(len(nums)-1):
            leftSum += nums[ind]
            
    
        pivot = -1
        point = len(nums)-1
        
        while point > -1:
            if leftSum == rightSum:
                pivot = point
                
            rightSum += nums[point]
            point-=1
            leftSum -= nums[point]
            
        
        return pivot
 