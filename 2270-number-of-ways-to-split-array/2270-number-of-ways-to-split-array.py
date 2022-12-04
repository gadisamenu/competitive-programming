class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        lgth = len(nums)-1
        
        valid_splits = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        for i in range(lgth):
            if nums[i] >= (nums[-1]-nums[i]):
                valid_splits +=1
                
        return valid_splits
        
            
            