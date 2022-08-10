class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        heap = [(0,(0,0),k)]
        DIR = [0,1,0,-1,0] 
        row = len(grid)
        col = len(grid[0])
        costs = [[float('inf')]* len(x) for x in grid]
        k_left =[[k]* len(x) for x in grid]
        is_valid = lambda r,c: -1 < r < row and -1 < c < col

        while heap:
            step,(r,c),left = heappop(heap)
            if left < 0:
                continue              
                
            if (r,c)  == (row-1,col-1):
                return step
            
            n_step = step +1
            for i in range(4):
                n_r = r + DIR[i]
                n_c = c + DIR[i+1]
                if is_valid(n_r,n_c) and (costs[n_r][n_c] > n_step or left -grid[n_r][n_c] > k_left[n_r][n_c]):
                    costs[n_r][n_c] = n_step
                    k_left[n_r][n_c] = left - grid[n_r][n_c]
                    heappush(heap,(n_step,(n_r,n_c),left-grid[n_r][n_c]))
   
        return -1
