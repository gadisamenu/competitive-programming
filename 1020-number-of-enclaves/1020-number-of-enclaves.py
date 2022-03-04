class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.DIR = [0,1,0,-1,0]
        self.cur_area= 0
        self.row= len(grid)
        self.col =len(grid[0])
        
        
        def dfs(ro,co):
            grid[ro][co] = 2
            for d in range(4):
                new_r, new_c = ro-self.DIR[d],co-self.DIR[d+1]
                if not isValid(new_r,new_c):
                    self.valid= False
                elif grid[new_r][new_c] == 1:
                    dfs(new_r,new_c)
            self.cur_area +=1
                
        isValid = lambda r,c: -1 < r < self.row and -1 <  c <  self.col
        
        #main function       
        self.enclaves =0
        for row in range(self.row):
            for col in range(self.col):
                if grid[row][col] == 1 :
                    self.valid = True
                    dfs(row,col)
                    if self.valid: self.enclaves +=self.cur_area
                    self.cur_area = 0
  
        return self.enclaves
    
