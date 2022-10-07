class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        isValid =  lambda r,c: -1 < r < row and -1 < c < col and obstacleGrid[r][c] == 0
        
        @cache
        def dp(r,c):
            if r == row-1 and c ==col-1:
                return 1
            ans = 0
            if isValid(r+1,c):ans +=  dp(r+1,c)
            if isValid(r,c+1):ans += dp(r,c+1)
                
            return ans
        
        return dp(0,0) if obstacleGrid[0][0] == 0 else 0
                
            
            
            