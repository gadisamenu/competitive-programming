class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []
        
        for i in range(len(strs)):
            counts.append(Counter(strs[i]))
        
#         @cache
#         def dp(i, m, n): 
#             if m < 0 or n < 0: return -float("inf")
#             if m == 0 and n == 0: return 0
#             if i >= len(strs):return 0
#             return max(1 + dp(i+1,m-counts[i]["0"], n-counts[i]["1"]),dp(i+1,m,n))
        
#         return dp(0,m,n)
    
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(len(strs)):
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j - counts[i]["0"] >= 0 and k - counts[i]["1"] >= 0:
                        dp[j][k] = max(dp[j][k], 1 + dp[j - counts[i]["0"]][k - counts[i]["1"]])
        
        # print(dp)
        return dp[-1][-1]
            
            
            