class Solution:
    def trap(self, height: List[int]) -> int:
        
        _max = 0
        right_max =deque()
        for i in range(1,len(height)+1):
            if height[-i] > _max: _max = height[-i]
            right_max.appendleft(_max)
            
        ans =0
        _max = 0
        for i in range(len(height)):
            if height[i] > _max:_max = height[i]
            ans -= height[i]
            if _max < right_max[i]: ans += _max
            else: ans += right_max[i] 
            
        return ans
            