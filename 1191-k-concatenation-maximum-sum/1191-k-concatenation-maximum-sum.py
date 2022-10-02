class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        lgth = len(arr)
        
        _max_sum = 0
        _max_left = 0
        _cur = 0
        
        for n in arr:
            _cur  += n
            _max_sum = max(_cur,_max_sum)
            if _cur < 0: _cur = 0
                
        if k == 1:
            return _max_sum % 1000000007
                  
        _max_left = 0
        _max_right = 0
        _lt_sm = 0
        _rt_sm  = 0
        for i in range(lgth):
            _lt_sm += arr[i]
            _rt_sm += arr[lgth-1-i]
            _max_left = max(_max_left,_lt_sm)
            _max_right = max(_max_right,_rt_sm)
            
            
        if k== 2: return max (_max_sum,_max_left+_max_right)% 1000000007
        
        _sum = sum(arr)
        return max(_max_sum,_max_left + _max_right + _sum*(k-2), _max_left+_max_right) % 1000000007
            