class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        _sum = 0
        _map = {0:-1}
        answer = 0
        for i in range(len(nums)):
            _sum +=  1 if nums[i] else -1
            
            if _sum in _map:
                answer = max(answer,i - _map[_sum])
            else:
                _map[_sum] = i
                
        return answer