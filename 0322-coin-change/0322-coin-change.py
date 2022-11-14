class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        value = defaultdict(lambda: float("inf"))
        value[0] = 0
        coins.sort()
        for birr in range(1,amount+1):
            for c in coins:
                if birr - c > -1:
                    value[birr] = min(value[birr],value[birr-c] + 1)
                    
        return -1 if value[amount]  == float("inf") else value[amount]
            
#         @cache
#         def dp(amt):
#             if amt > amount: return float("inf")
#             if amt == amount: return 0
#             ans = float(inf)
#             for n in coins:
#                 ans = min(ans,dp(amt+n))
#             return  1 +  ans
        
#         ret = dp(0)
#         return -1 if ret == float("inf") else ret