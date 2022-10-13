class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1 
        right = len(nums)-1
        
        while left <= right:
            m = left + (right-left)//2
            
            lefts = 0            
            for num in nums:
                if num <= m:
                    lefts += 1
              
            if lefts > m:
                right = m
            else:
                left = m+1
            if left == right ==m:
                break
            
        return m
                
            
        