class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def dfs(lv,hv):
            
            if lv == hv: return 1
            if lv > hv:return 1
            chld = 0
            for i in range(lv,hv+1):
                chld += dfs(lv,i-1) * dfs(i+1,hv)
            return chld
        
        return dfs(1,n)
                
    
            
            