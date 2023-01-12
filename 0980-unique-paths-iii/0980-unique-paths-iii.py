class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.DIR=[0,1,0,-1,0]
        self.answer = 0
        self.is_valid = lambda r,c,vstd: -1 < r < row and -1 < c < col and vstd & 1<<(r*col + c)
        row = len(grid)
        col = len(grid[0])
        all_visited = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0 or grid[r][c] == 2:
                    if all_visited & 1 <<(r*col + c):
                        print(r,c)
                    all_visited |= 1<<(r*col + c)
                elif grid[r][c] == 1:
                    start = r,c
        self.findUniquePaths(start[0],start[1],grid,all_visited,col)
        return self.answer
    
    def findUniquePaths(self,row,col,grid,visited,number_col):
        if grid[row][col] == 2:
            if not visited:
                self.answer += 1
        else:
            for d in range(4):
                new_row = row + self.DIR[d]
                new_col = col + self.DIR[d+1]
                if self.is_valid(new_row,new_col,visited):
                    visited &= ~(1<<(new_row*number_col + new_col))
                    self.findUniquePaths(new_row,new_col,grid,visited,number_col)
                    visited |= 1<<(new_row*number_col + new_col)
                
        
        
        
                    
                    
                    
                    
                    
                