class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        pre = 2
        answer = []
        for i in range(len(nums)-1):
            difference = nums[i+1] - nums[i]
            if difference > 1 and pre > 1:
                answer.append(nums[i])
            pre = difference
            
        if pre > 1:answer.append(nums[-1])
            
        return answer
            
        
                
            