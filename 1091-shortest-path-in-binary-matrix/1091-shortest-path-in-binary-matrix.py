class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row= len(grid)
        DIR = [0,1,1,-1,-1,1,0,-1,0]
        
        if grid[0][0] != 0:
            return -1
        

        isValid= lambda r,c: 0<= r < row and 0<= c < row
        que = deque([(0,0,1)])
        
        while que:
            
            cur = que.popleft()
            if (cur[0],cur[1]) == (row-1,row-1):
                return cur[2]
        
            for d in range(len(DIR)-1):
                n_r= cur[0]+DIR[d]
                n_c= cur[1]+DIR[d+1]
                
                if isValid(n_r,n_c) and grid[n_r][n_c] == 0:
                    grid[n_r][n_c]= 1
                    que.append((n_r,n_c,cur[2]+1))
            
        return -1