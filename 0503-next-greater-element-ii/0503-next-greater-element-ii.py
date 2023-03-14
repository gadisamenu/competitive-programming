class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lgth = len(nums)
        stack = []
        answer = [-1 for _ in range(lgth)]
        
        for i in range(lgth):
            while stack and nums[stack[-1]] < nums[i]:
                answer[stack.pop()] = nums[i]
            stack.append(i)
            
        i = 0
        while stack and i < lgth:
            while stack and nums[stack[-1]] < nums[i]:
                answer[stack.pop()] = nums[i]
                
            i += 1
            
        return answer