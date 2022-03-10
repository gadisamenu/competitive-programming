class Solution:
   
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lgth = len(cost)
        
        @lru_cache()
        def helper(idx):
            if (idx +2 >= lgth) or (idx + 1 >= lgth):
                return cost[idx]
            one = helper(idx+1)
            two = helper(idx+2)
            
            return cost[idx]+ min(one,two)
    
        return min(helper(0),helper(1))