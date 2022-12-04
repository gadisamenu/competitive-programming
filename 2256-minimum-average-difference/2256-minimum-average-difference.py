class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            
        value = float("inf")
        answer = 0
        lgth = len(nums)
        for i in range(lgth-1):
            cur = abs(nums[i]//(i+1) - (nums[-1] -nums[i])//(lgth-i-1))
            if value > cur:
                answer = i
                value = cur
        
        last = abs((nums[-1]//lgth)-0)
        if last < value:
            answer = lgth-1
            
        return answer
            
        
            
        