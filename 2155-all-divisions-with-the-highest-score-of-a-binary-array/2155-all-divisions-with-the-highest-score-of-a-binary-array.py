class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        one_ct = 0
        for n in nums:
            if n == 1: one_ct += 1
                
        ans = [one_ct,[0]]
        
        zero_ct = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_ct += 1
            else: one_ct -= 1
            
            scr = zero_ct + one_ct
            if scr == ans[0]: ans[1].append(i+1)
            elif scr > ans[0]:ans = [scr,[i+1]]
                
                
        return ans[1]
            
            