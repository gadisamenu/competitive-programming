class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        q = deque([start])
        
        visited.add(start)
        
        while q:
            
            cur = q.popleft()
           
            if arr[cur] == 0:
                return True
            up = cur+arr[cur]
            down = cur-arr[cur]
            print(up,down)
           
            if up < len(arr) and up not in visited:
                q.append(up) 
                visited.add(up)
            if down >= 0 and down not in visited: 
                q.append(down)
                visited.add(down)
            
        return False