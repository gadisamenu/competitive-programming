class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pref_sum = [0]
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            pref_sum.append(_sum)
   
        incr_que = deque()
        ans = float("inf")
        
        for i in range(len(pref_sum)):
            while incr_que and pref_sum[incr_que[-1]] > pref_sum[i]:
                incr_que.pop()
                
            incr_que.append(i)
            while incr_que and pref_sum[i] - pref_sum[incr_que[0]] >= k:
                ans = min(ans,i-incr_que.popleft())
        
        return -1 if ans == float("inf") else ans
                
