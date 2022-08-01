class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def dfs(row,col):
            if row == m -1 and col == n - 1:
                return 1
            
            path = 0
            
            if row + 1 < m :path +=  dfs( row + 1, col)
                    
            if col + 1 < n :path += dfs( row , col + 1)
                
            return path
        
        return dfs(0,0)