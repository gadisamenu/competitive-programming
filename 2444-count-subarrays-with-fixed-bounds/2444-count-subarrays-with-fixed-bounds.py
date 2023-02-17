class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lgth = len(nums)
        answer  = 0
        last_invalid = -1 
        min_start = -1
        max_start = -1 
        
        for i in range(lgth):
            if (nums[i] < minK or nums[i] > maxK):
                last_invalid = i
            if (nums[i] == maxK):
                max_start = i
            if (nums[i] == minK):
                min_start = i
            
            count = min(min_start,max_start) - last_invalid;
            answer += max(0,count)
            
        return answer