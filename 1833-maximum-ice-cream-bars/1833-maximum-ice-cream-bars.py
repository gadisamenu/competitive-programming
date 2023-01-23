class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        _max = max(costs)+1
        count = [0 for i in range(_max)]
        for cost in costs:
            count[cost] += 1
        
        bars = 0
        index = 1
        while coins >= index and index < _max:
            cap = coins//index
            used = min(cap,count[index])
            coins -= index *used
            bars += used
            index += 1
        return bars
            
            
#         costs.sort()
#         bars = 0
#         cost = 0
#         for i in range(len(costs)):
#             cost += costs[i]
#             if cost <= coins:
#                 bars += 1
#             else:
#                 break
#         return bars
            