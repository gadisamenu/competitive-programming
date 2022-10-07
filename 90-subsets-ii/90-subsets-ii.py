class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        path = []
        def backTracking(l):
            ans.add(tuple(sorted(path)))
            for i in range(l+1,len(nums)):
                path.append(nums[i])
                backTracking(i)
                path.pop()
            
            
        backTracking(-1)
        return ans
            
                
                
                
        