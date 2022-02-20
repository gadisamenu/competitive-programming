from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lgth = len(nums)
        incr = deque((0,))
        decr = deque((0,))
        i = 0
        j = 0
        longst = 0
        while j < lgth:
            mini = incr[0] if incr else 0
            maxi = decr[0] if decr else 0
            
            if nums[maxi] - nums[mini] <= limit:
                longst = (j - i+1) if (j -i +1) > longst else longst
                
                if j < (lgth-1):
                    j += 1
                else:
                    break
                
                while incr and nums[incr[-1]] > nums[j]:
                    incr.pop()
                while decr and nums[decr[-1]] < nums[j]:
                    decr.pop()
                    
                incr.append(j)
                decr.append(j)
                
            else:
                if incr and incr[0] == i:
                    incr.popleft()
                if decr and decr[0] == i:
                    decr.popleft()
                i +=1
                    
        return longst
        