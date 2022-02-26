class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        op = 0
        i = 0
        j = 0
        max_con = 0
        while j < len(nums):
            
            if nums[j] == 1:
                max_con = max(max_con,j-i+1)
                j+=1
                
                
            elif nums[j] == 0:
                if op < k:
                    max_con  = max(max_con,j-i+1)
                    j+=1
                    op += 1
                else:
                    while nums[i] == 1:
                        i += 1
                    i += 1
                    max_con = max(max_con,j-i+1)
                    j += 1
                    
        return max_con
            
            
        