class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        
        left = 0
        right = nums[-1] - nums[0]
        
        while left < right:
            mdl = left + (right - left)//2
            
            count= self.count_pairs(nums,mdl)
            
            if count < k:
                left = mdl + 1
                
            else:
                right = mdl
                
        return left 
    
    
    def count_pairs(self,nums,distance):
        count = 0
        start = 0
        for end in range(len(nums)):
            while abs(nums[end] - nums[start]) > distance:
                start += 1
                
            count += (end - start)     
        return count
        
        