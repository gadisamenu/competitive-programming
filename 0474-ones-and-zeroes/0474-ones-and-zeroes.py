class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []
        
        for i in range(len(strs)):
            counts.append(Counter(strs[i]))
        
        @cache
        def dp(i, m, n):
            if m < 0 or n < 0: return -float("inf")
            if m == 0 and n == 0: return 0
            if i >= len(strs):return 0
            return max(1 + dp(i+1,m-counts[i]["0"], n-counts[i]["1"]),dp(i+1,m,n))
        
        return dp(0,m,n)
            
            
            
            