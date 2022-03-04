class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        heap = []
        heappush(heap,(grid[0][0],0,0))
        time = 0
        while heap:
            cur = heappop(heap)
            time = cur[0] if cur[0] >time else time
            
            if (cur[1],cur[2])== (row-1,row-1):
                return time 
            
            grid[cur[1]][cur[2]] = -1
            
            if cur[1]-1 >=0 and  grid[cur[1]-1][cur[2]] > -1: 
                heappush(heap,( grid[cur[1]-1][cur[2]] , cur[1]-1,cur[2]))
                
            if cur[1]+1 < row and grid[cur[1]+1][cur[2]] > -1: 
                heappush(heap,( grid[cur[1]+1][cur[2]] , cur[1]+1,cur[2]))
                
            if cur[2]-1 >=0 and grid[cur[1]][cur[2]-1] > - 1: 
                heappush(heap,( grid[cur[1]][cur[2]-1] , cur[1],cur[2]-1))
                
            if cur[2]+1 < row and grid[cur[1]][cur[2]+1] > - 1: 
                heappush(heap,( grid[cur[1]][cur[2]+1] , cur[1],cur[2]+1))
        