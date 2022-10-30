class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_mins = deque()
        _min = float("inf")
        for i in range(len(nums)-1,-1,-1):
            _min = min(_min,nums[i])
            left_mins.appendleft(_min)
    
        _max = 0
        for i in range(len(nums)-1):
            _max = max(nums[i],_max)
            if _max <= left_mins[i+1]:
                return i+1
        
            