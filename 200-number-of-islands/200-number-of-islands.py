class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        
        for i in range(row):
            for j  in range(col):
                if grid[i][j] == "1":
                    count += 1
                    stack = [(i,j)]
                    grid[i][j] = 0 
                    while stack:
                        r,c = stack.pop()
                        
                        if r + 1 < row and grid[r+1][c] == "1": 
                            stack.append((r+1,c))
                            grid[r+1][c] = "0"
                        if r - 1 > -1 and grid[r-1][c] == "1":
                            stack.append((r-1,c))
                            grid[r - 1][c] = "0"
                        if c + 1 < col and grid[r][c+1] == "1":
                            grid[r][c + 1] = "0"
                            stack.append((r,c+1))
                        if c - 1 > -1 and grid[r][c-1] == "1": 
                            stack.append((r,c-1))
                            grid[r][c-1] = "0"
                            
        return count

            