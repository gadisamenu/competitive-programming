class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        @cache
        def dp(chrr:str,ind:int):
            if ind == 1:
                return 1
            if chrr == "a":
                return dp("e",ind-1)
            ans = 0
            if chrr == "e":
                ans += dp('a',ind-1)
                ans += dp('i',ind-1)
            elif chrr == "i":
                for n in ["a","e","o","u"]:
                    ans += dp(n,ind - 1)
            elif chrr == "o":
                ans += dp('i',ind - 1)
                ans += dp('u',ind - 1)
                
            elif chrr == 'u':
                ans += dp('a',ind - 1)
            return ans
        
        ans = 0
        for cr in ['a','e','i','o','u']:
            ans = (ans +  dp(cr,n)) % (1000000007)
        return ans  % (1000000007)
                
                