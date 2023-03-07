class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1000000007
        
        @cache
        def dp(top_lgth,bottom_lgth):
            if top_lgth > 0 and bottom_lgth > 0:
                if top_lgth > bottom_lgth:
                    return (dp(top_lgth - 2,bottom_lgth) + dp(top_lgth - 2,bottom_lgth - 1))%mod
                  
                if top_lgth < bottom_lgth:
                    return (dp(top_lgth,bottom_lgth - 2) + dp(top_lgth - 1,bottom_lgth - 2))%mod
                
                
                return (dp(top_lgth- 1,bottom_lgth - 1) + dp(top_lgth -2 ,bottom_lgth - 2) + dp(top_lgth - 1,bottom_lgth - 2) + dp(top_lgth - 2,bottom_lgth - 1))%mod
                
            return 1 if top_lgth == 0 and bottom_lgth == 0 else 0
        
        return dp(n,n)%mod
        