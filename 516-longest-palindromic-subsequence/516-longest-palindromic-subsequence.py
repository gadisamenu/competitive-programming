class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:        
        @cache
        def dp(lft,rgt):
            if lft > rgt:
                return 0
            if lft == rgt:
                return 1
            if lft - rgt == 1:
                return 2 if s[lft]== s[rgt] else 0
            if s[lft] == s[rgt]:
                return  max(dp(lft+1,rgt-1),dp(lft +2,rgt-1), dp(lft+1,rgt-2)) + 2
            return max(dp(lft,rgt-1),dp(lft +1,rgt))

        return dp(0,len(s)-1)