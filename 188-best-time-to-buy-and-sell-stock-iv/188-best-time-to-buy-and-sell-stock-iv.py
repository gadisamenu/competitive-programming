class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k == 0 or n <= 1:
            return 0
        if 2*k > n:
            res = 0
            for i in range(n-1):
                if prices[i+1] > prices[i]:
                    res += prices[i+1] - prices[i]
            return res
        mini = -(10**9)
        dp  = [0 for i in range(2*k)]
        dp[0] = -prices[0]
        for i in range(2*k):
            if i%2 == 0:
                dp[i] = mini
        
        for i in range(n):
            for j in range(2*k):
                if j == 0:
                    dp[j] = max(dp[j],-prices[i])
                elif j % 2 == 0:
                    dp[j] = max(dp[j],dp[j-1] - prices[i])
                else:
                    dp[j] = max(dp[j],dp[j-1] + prices[i])
        return dp[-1]