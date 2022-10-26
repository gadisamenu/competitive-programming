class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def isValid(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid)
        
        def distance(row1, col1, row2, col2):
            return abs(row2-row1) + abs(col2 - col1)
        
        
        
      
        n = len(grid)
        queue = deque()
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    queue.append((i,j, i, j ))
                  
                
        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        if not queue:
            return -1
        if len(queue)==n*n:
            return -1
        
        
        while queue:
            curx, cury, parentx, parenty = queue.popleft()
            
            for dx, dy in direction:

                new_row, new_col = dx + curx, dy + cury

                if isValid(new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, parentx, parenty))
            
        return distance(curx, cury, parentx, parenty)