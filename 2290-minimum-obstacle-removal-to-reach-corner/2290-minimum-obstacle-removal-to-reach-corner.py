class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        heap = [(0,(0,0))]
        DIR = [0,1,0,-1,0] 
        row = len(grid)
        col = len(grid[0])
        costs = [[float('inf')]* len(x) for x in grid]
        is_valid = lambda r,c: -1 < r < row and -1 < c < col

        while heap:
            obst,(r,c) = heappop(heap)

            if (r,c)  == (row-1,col-1):
                return obst

            for i in range(4):
                n_r = r + DIR[i]
                n_c = c + DIR[i+1]
                if is_valid(n_r,n_c):
                    n_obst = obst + grid[n_r][n_c]
                    if costs[n_r][n_c] > n_obst:
                        costs[n_r][n_c] =  n_obst
                        heappush(heap,(n_obst,(n_r,n_c))) 



