class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum_s = 0
        
        i = 0
        
        while i < len(nums)-1:
            j = i
            max_im = nums[i]
            min_m = nums[i]
            while j < len(nums):
                if nums[j] > max_im: max_im = nums[j]
                if nums[j] < min_m: min_m = nums[j]
                sum_s += (max_im - min_m)
                j+=1
            i+=1
            
        return sum_s
                
            
        
            
            