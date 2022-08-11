class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(ind:int,buyed = -1):
            if ind >= len(prices):return 0
            if buyed != -1:
                return max(prices[ind]-buyed+dp(ind+2),dp(ind+1,buyed))
            return max(dp(ind+1,prices[ind]),dp(ind+1))
            
        return dp(0)