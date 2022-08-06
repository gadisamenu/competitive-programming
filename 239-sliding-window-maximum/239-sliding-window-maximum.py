class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        
        for n in range(k):
            while queue and nums[queue[-1]] <= nums[n]:
                queue.pop()
            queue.append(n)
            
        ans = []
        
        for ind in range(k,len(nums)):
            ans.append(nums[queue[0]])
            
            while queue and nums[queue[-1]] <= nums[ind]:
                queue.pop()
            queue.append(ind)
            
            if queue and queue[0] == ind -k:
                queue.popleft()
                
        ans.append(nums[queue[0]])
        
        return ans
                        
            
            