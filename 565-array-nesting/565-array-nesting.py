class Solution:
    def arrayNesting(self, nums: List[int]) -> int:          
        
        visited = set()
        lgth =0
        for i in range(len(nums)):
            if i not in visited:
                _nxt = i
                cur_lgth = 0
                while True:
                    if _nxt in visited: break
                    visited.add(_nxt)
                    _nxt = nums[_nxt]
                    cur_lgth += 1
                    
                lgth = max(lgth,cur_lgth)
        
        return lgth
            