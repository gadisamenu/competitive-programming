class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        _max = max(cost1,cost2)
        _min = min(cost1,cost2)
        
        ans = 1
        while total >= _min:
            ans += total//_min
            if total >= _max:
                ans += 1
            total -= _max
        return ans