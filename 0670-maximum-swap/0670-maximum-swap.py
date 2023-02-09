class Solution:
    def maximumSwap(self, num: int) -> int:
    
        num = list(str(num))
        
        left = len(num)
        found = None
        _max = len(num) - 1
        
        for i in range(len(num)-1,-1,-1):
            if num[i] < num[_max]:
                found = _max
                left = i
            elif num[i] > num[_max]:
                _max = i
        if found:
            num[left],num[found] = num[found],num[left]
     
        return int("".join(num))
                
            