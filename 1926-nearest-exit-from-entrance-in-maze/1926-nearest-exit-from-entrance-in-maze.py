class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        DIR = [0,1,0,-1,0]
        in_bound = lambda r,c: -1 < r < rows and -1 < c < cols
        
        queue = deque([tuple(entrance)])
        maze[entrance[0]][entrance[1]] = "+"
        
        moves = 0
        while queue:
            lgth = len(queue)
            while lgth:
                row,col  = queue.popleft()
                
                for d in range(4):
                    n_row = row + DIR[d]
                    n_col = col + DIR[d+1]
                    
                    if in_bound(n_row,n_col):
                        if maze[n_row][n_col]==".":
                            queue.append((n_row,n_col))
                            maze[n_row][n_col] = "+"
                    elif row != entrance[0] or col != entrance[1]:
                        return moves
                    
                lgth -= 1
            moves += 1
        
        return -1