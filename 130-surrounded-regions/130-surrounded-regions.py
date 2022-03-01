class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.DIR = [0,1,0,-1,0]
        """
        Do not return anything, modify board in-place instead.
        """
            
        self.row= len(board)
        self.col =len(board[0])
        
        def dfs(ro,co):
            self.visited.add((ro,co))
            self.region.add((ro,co))
            for d in range(len(self.DIR)-1):
                new_r, new_c = ro-self.DIR[d],co-self.DIR[d+1]
                if out_bound(new_r,new_c):
                    self.valid= False
                    continue
               
                if board[new_r][new_c] == 'O' and  (new_r,new_c) not in self.region:
                    dfs(new_r,new_c)
                
        out_bound = lambda r,c: r < 0 or r >= self.row or c < 0 or c >= self.col
        
         #main function       
        self.region = set()
        self.visited = set()
        for row in range(self.row):
            for col in range(self.col):
                if board[row][col] == 'O' and (row,col) not in self.visited:
                    self.valid = True
                    dfs(row,col)
                    
                    if self.valid:
                        for ro,co in self.region:
                            board[ro][co] = "X"
                            
                    self.region.clear()
                    
 
     