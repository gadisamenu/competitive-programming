class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        path = []
        def backtracking(i):
            if i == len(nums):
                if len(path) > 1:
                    answer.add(tuple(path))
                return 
            if not path or path[-1] <= nums[i]:
                path.append(nums[i])
                backtracking(i+1)
                path.pop()
                
            backtracking(i+1)
            
        backtracking(0)
        return answer
        
            