class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        DIR= [0,1,0,-1,0]
        is_valid= lambda r,c: -1 < r < row and -1 < c < col and grid[r][c] == 1
        visited = set()
        
        def recursion(r,c):
            ans =  0
            for i in range(4):
                n_r = r + DIR[i]
                n_c = c + DIR[i+1]
        
                if is_valid(n_r,n_c):
                     
                    if (n_r,n_c) not in visited:
                        visited.add((n_r,n_c))
                        ans += recursion(n_r,n_c)
                else: ans += 1
            return ans
        
        for n in range(row):
            for m in range(col):
                if grid[n][m] == 1:
                    visited.add((n,m))
                    return recursion(n,m)
                
                