class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amt):
            if amt < 0: return float("inf")
            if amt == 0: return 0
            ans = float(inf)
            for n in coins:
                ans = min(ans,dp(amt-n))
            return  1 +  ans
        
        ret = dp(amount)
        return -1 if ret == float("inf") else ret