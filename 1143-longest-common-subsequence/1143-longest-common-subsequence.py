class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for i in range(len(text2)+1)]
        cur = [0 for i in range(len(text2)+1)]
        for i in range(0,len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    cur[j+1] = 1 + dp[j]
                else:
                    cur[j+1] = max(dp[j+1],cur[j])
            temp = dp
            dp = cur
            cur = temp
            
        return dp[len(text2)]
    
    