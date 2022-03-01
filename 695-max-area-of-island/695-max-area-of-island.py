class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        max_area= 0

        def dfs(r,c):
            self.cur_area+=1
            grid[r][c] = 0
            if r-1 >= 0 and  grid[r-1][c] == 1:
                dfs(r-1,c)
                
            if r+1 < row and grid[r+1][c] == 1:
                dfs(r+1,c)
                
            if  c-1 >= 0 and grid[r][c-1] == 1:
                dfs(r,c-1)
                
            if  c+1 < col and grid[r][c+1] == 1:
                dfs(r,c+1)

        
        for ro in range(row):
            for co in range(col):
                self.cur_area = 0
                if grid[ro][co] == 1:
                    dfs(ro,co)
                    max_area = max(max_area,self.cur_area)
        
        return max_area

 