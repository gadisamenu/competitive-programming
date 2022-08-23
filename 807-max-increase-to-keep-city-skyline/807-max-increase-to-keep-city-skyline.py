class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.max = [[0 for n in range(len(grid))],[0 for n in range(len(grid))]]

        def dp(i:int,j:int):
            if (i,j) in visited:
                return
            visited.add((i,j))
            if i+1 < len(grid): dp(i+1,j)
            if j+1 < len(grid): dp(i,j+1) 
            self.max[0][i]  = max(self.max[0][i] ,grid[i][j])
            self.max[1][j]  = max(self.max[1][j] ,grid[i][j])
            
        
        def build(i:int,j:int):
            if  (i,j) in visited:
                return 
            visited.add((i,j))
            self.ans += (min(self.max[0][i],self.max[1][j]) - grid[i][j])
            if i+1 < len(grid): build(i+1,j)
            if j+1 < len(grid): build(i,j+1) 
                
        visited = set()
        dp(0,0)
        visited = set()
        build(0,0)        
        return self.ans