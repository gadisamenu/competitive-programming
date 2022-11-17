class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(ind:int,bought= False):
            if ind >= len(prices):
                return 0
            if bought:
                return max(prices[ind] + dp(ind+1),dp(ind+1,True))
            return max(dp(ind+1,True)-prices[ind],dp(ind+1))
                    
        return dp(0)