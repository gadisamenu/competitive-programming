class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = []
        for i in range(len(grid[0])):
            answer.append(self.move(0,i,grid))
            
        return answer
    
    def move(self,r,c,box):
        if r + 1 >  len(box):
            return c
        if box[r][c] == 1:
            if c + 1 < len(box[0]) and box[r][c+1] == 1:
                return self.move(r+1,c+1,box)
            return -1
        elif c -1 > -1 and box[r][c-1] == -1:
            return self.move(r+1,c-1,box)
        return -1 
            