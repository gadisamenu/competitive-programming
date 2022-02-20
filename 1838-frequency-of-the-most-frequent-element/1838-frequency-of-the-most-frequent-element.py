import math
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        
        lgth = len(nums)
        
        frq = 1
        total = nums[0]
        
        i = 0
        j = 1
        if j < lgth :
            total += nums[j]
        
        while j < lgth:
            area = nums[j] * (j-i +1)
            if area - total  <= k:
                if frq < j-i+1 :
                    frq = j-i + 1
                j +=1
                if j < lgth:
                    total += nums[j]
                
            else:
                total -= nums[i]
                i += 1
      
            
        return frq
        