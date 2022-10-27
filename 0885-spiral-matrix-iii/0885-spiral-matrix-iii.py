class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    
        isvalid_move = lambda r,c: -1 < r < rows and -1 < c < cols
        
        next_direction = {"up":"right","down":"left","right":"down","left":"up"}
        next_cell = {"up":(-1,0),"down":(1,0),"right":(0,1),"left":(0,-1)}
        
        direction = "right"
        answer = []
        bound = rows*cols
        moves_lgth = 1
        moves_left = 1
        row = rStart
        col = cStart

        while len(answer) < bound:
            if isvalid_move(row,col):
                answer.append((row,col))

            if not moves_left:
                if direction == "up" or direction == "down":
                    moves_lgth += 1
                moves_left = moves_lgth          
                direction=  next_direction[direction]
                
            row += next_cell[direction][0]
            col += next_cell[direction][1]
            moves_left -= 1
            

        return answer
            
            
            
            