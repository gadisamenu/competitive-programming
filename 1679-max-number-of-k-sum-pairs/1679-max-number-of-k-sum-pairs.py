class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
                      
        opps = 0
        
        i = 0 
        j = len(nums)-1
        
        while j>i:
            addi= nums[j] + nums[i]
            if addi == k:
                opps+=1
                j -= 1
                i += 1
            elif addi < k:
                i += 1
            elif addi > k:
                j -= 1
        return opps
                
        
