class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1 
        right = len(nums)-1
        
        while left <= right:
            m = left + (right-left)//2
            
            lefts = 0
            rights = 0
            
            for num in nums:
                if left <= num <= m:
                    lefts +=1
                elif num <= right:
                    rights +=1
                    
            if lefts > m-left+1:
                right = m
            else:
                left = m+1
            if left == right ==m:
                break
            
        return m
                
            
        