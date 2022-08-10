class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0],(0,0))]
        row = len(grid)
        col = len(grid[0])
        costs = [[float('inf')]* len(x) for x in grid]

        while heap:
            cost,(r,c) = heappop(heap)       
                
            if (r,c)  == (row-1,col-1):
                return cost
            
            if r+1 <  row and costs[r+1][c] > cost+ grid[r+1][c]:
                costs[r+1][c] = cost + grid[r+1][c]
                heappush(heap,(costs[r+1][c],(r+1,c)))
                
            if c+1 < col and costs[r][c+1] >cost +grid[r][c+1]:
                costs[r][c+1] = cost + grid[r][c+1]
                heappush(heap,(costs[r][c+1],(r,c+1)))
                