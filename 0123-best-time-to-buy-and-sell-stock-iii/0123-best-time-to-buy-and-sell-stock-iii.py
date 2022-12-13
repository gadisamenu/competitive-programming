class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        index,state,transactions
        10^5   2        2
        
        
        """
        @cache        
        def dp(index,selling,transactions):
            if not transactions:
                return 0
            if index == len(prices):
                return 0
            if selling:
                return max(dp(index+1,True,transactions), prices[index] + dp(index+1,False,transactions-1))
            return max(dp(index + 1, False,transactions), -prices[index] +  dp(index+1,True,transactions))
                       
                       
        return dp(0,False,2)