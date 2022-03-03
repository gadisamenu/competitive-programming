class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [0,1,0,-1,0]
        
        row = len(grid)
        col = len(grid[0])
        q = deque()
        visited = []
        cur=[0,0,0]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    visited.append((i,j))
                    q.append((i,j,0))
                elif grid[i][j]== 0:
                    visited.append((i,j))

        isValid = lambda r,c: -1 < r < row  and -1 < c < col
        
        while q:
            cur = q.popleft()
            for d in range(len(DIR)-1):
                ro = cur[0] + DIR[d]
                co = cur[1] + DIR[d+1]
                
                if isValid(ro,co) and grid[ro][co] == 1:
                    grid[ro][co] = 2
                    visited.append((ro,co))
                    q.append((ro,co,cur[2]+1))
                    
        
        return cur[2] if len(visited)== row*col else -1

                
                
                
                    
            
        
                
        
        
                
                