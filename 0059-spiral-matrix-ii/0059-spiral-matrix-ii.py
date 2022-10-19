class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        isvalid_move = lambda r,c: -1 < r < n and -1 < c < n and matrix[r][c] == 0
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        next_direction = {"up":"right","down":"left","right":"down","left":"up"}
        next_cell = {"up":(-1,0),"down":(1,0),"right":(0,1),"left":(0,-1)}
        break_point = n**2+1
        current_number = 1
        direction = "right"
        
        row = 0
        col = 0
        while current_number != break_point:             
            matrix[row][col] = current_number
            
            current_number += 1
            next_row = row + next_cell[direction][0]
            next_col = col + next_cell[direction][1]
            
            if not isvalid_move(next_row,next_col):
                direction=  next_direction[direction]
                next_row = row + next_cell[direction][0]
                next_col = col + next_cell[direction][1]
                
            row = next_row
            col = next_col
    
    
        return matrix
            
            
            
            