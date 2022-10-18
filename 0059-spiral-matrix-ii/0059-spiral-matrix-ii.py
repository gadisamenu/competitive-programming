class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        break_point= n**2
        isvalid_move = lambda r,c: -1 < r < n and -1 < c < n and matrix[r][c] == 0
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        next_direction = {"up":"right","down":"left","right":"down","left":"up"}
        next_cell = {"up":(-1,0),"down":(1,0),"right":(0,1),"left":(0,-1)}
        
        self.invalid = 0
        self.current_number = 1
        self.direction = "right"
        def fill_cell(row,col):
            matrix[row][col] = self.current_number
            
            next_row = row + next_cell[self.direction][0]
            next_col = col + next_cell[self.direction][1]

            if isvalid_move(next_row,next_col):
                self.invalid = 0
                self.current_number += 1
                fill_cell(next_row,next_col)
            else:
                self.invalid +=1
                if self.invalid  > 1:return 
                self.direction=  next_direction[self.direction]
                fill_cell(row,col)
                
        fill_cell(0,0)
    
        return matrix
            
            
            
            