class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        visited=set()
        
        moves=0
        queue=deque([])
        count_keys=0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="@":
                    queue.append((i,j,''))
                elif grid[i][j].islower():
                    count_keys+=1
        
        while queue:
            for _ in range(len(queue)):
                curr_x,curr_y,keys = queue.popleft()
                if (curr_x,curr_y,keys) in visited:
                    continue
                
                visited.add((curr_x,curr_y,keys))
                
                if len(keys)==count_keys:
                    return moves
                
                for x,y in ((0,1),(1,0),(-1,0),(0,-1)):
                    nx=curr_x+x
                    ny=curr_y+y
                    if nx<0 or ny<0 or nx>=m or ny>=n or grid[nx][ny]=='#' or (nx,ny,keys) in visited:
                        continue
                        
                    curr=grid[nx][ny]                    
                    if curr in 'abcdef' and curr not in keys:
                        queue.append((nx,ny,keys+curr))                            
                    elif curr.isupper() and curr.lower() not in keys:
                        continue
                    else:
                        queue.append((nx,ny,keys))
            moves+=1
        
        return -1