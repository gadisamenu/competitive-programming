class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def dp(lv,hv):
            
            if lv == hv: return 1
            if lv > hv:return 1
            chld = 0
            for i in range(lv,hv+1):
                chld += dp(lv,i-1) * dp(i+1,hv)
            return chld
        
        return dp(1,n)
                
    
            
            