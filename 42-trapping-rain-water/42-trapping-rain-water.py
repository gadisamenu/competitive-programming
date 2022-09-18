class Solution:
    def trap(self, height: List[int]) -> int:
        
        _max = 0
        right_max =deque()
        for i in range(1,len(height)+1):
            _max = max(height[-i],_max)
            right_max.appendleft(_max)
            
        ans =0
        _max = 0
        for i in range(len(height)):
            _max = max(_max,height[i])
            ans += min(_max,right_max[i]) - height[i]
            
        return ans
            