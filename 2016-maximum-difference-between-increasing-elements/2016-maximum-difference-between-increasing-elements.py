class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = - 1
        
        _min = nums[0]
        
        for i in range(1,len(nums)):
            if _min >= nums[i]:
                _min = nums[i]

            else:
                answer = max(answer,nums[i] - _min)
                
        return answer
                