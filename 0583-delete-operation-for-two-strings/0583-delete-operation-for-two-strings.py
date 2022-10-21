class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0 for i in range(len(word2)+1)]
        cur = [0 for i in range(len(word2)+1)]
        
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    cur[j+1]= 1+ dp[j]
                else:
                    cur[j+1] = max(dp[j+1],cur[j])
            temp = dp
            dp = cur
            cur = temp

        return len(word1) + len(word2) - 2*dp[len(word2)]
    
    