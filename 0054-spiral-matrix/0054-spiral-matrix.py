class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        colums = len(matrix[0])
        isvalid_move = lambda r,c: -1 < r < rows  and -1 < c < colums and matrix[r][c] < 200
        
        answer = []
        next_direction = {"up":"right","down":"left","right":"down","left":"up"}
        next_cell = {"up":(-1,0),"down":(1,0),"right":(0,1),"left":(0,-1)}
        
        self.direction = "right"
        
        def fill_cell(row,col):
            
            if len(answer)== rows*colums:
                return answer 
            
            answer.append(matrix[row][col])
            matrix[row][col]+= 201
            
            next_row = row + next_cell[self.direction][0]
            next_col = col + next_cell[self.direction][1]
            
            if not isvalid_move(next_row,next_col):
                self.direction=  next_direction[self.direction]
                next_row = row + next_cell[self.direction][0]
                next_col = col + next_cell[self.direction][1]
                
            return fill_cell(next_row,next_col)
                

        return fill_cell(0,0)
    
  
            
            
            
            