class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        isvalid_move = lambda r,c: -1 < r < n and -1 < c < n and matrix[r][c] == 0
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        next_direction = {"up":"right","down":"left","right":"down","left":"up"}
        next_cell = {"up":(-1,0),"down":(1,0),"right":(0,1),"left":(0,-1)}
        self.break_point = n**2+1
        self.current_number = 1
        self.direction = "right"
        
        def fill_cell(row,col):
            if self.current_number == self.break_point:
                return 
            matrix[row][col] = self.current_number
            self.current_number += 1
            next_row = row + next_cell[self.direction][0]
            next_col = col + next_cell[self.direction][1]
            
            if not isvalid_move(next_row,next_col):
                self.direction=  next_direction[self.direction]
                next_row = row + next_cell[self.direction][0]
                next_col = col + next_cell[self.direction][1]
                
            fill_cell(next_row,next_col)
        
        fill_cell(0,0)
    
        return matrix
            
            
            
            