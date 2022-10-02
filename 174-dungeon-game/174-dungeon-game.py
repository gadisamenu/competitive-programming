class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon) -1
        col = len(dungeon[0])-1
        ans = 1
        heap = [(-dungeon[0][0],0,0)]
        costs = defaultdict(lambda:float("inf"))
        costs[(0,0)] = -dungeon[0][0] 
        
        while heap:
            cost,r,c = heappop(heap)
            ans = max(cost+1,ans)
            if r== row and c == col: break
            
            rn= r+1
            cn = c+1
            if rn <= row:
                nc = cost - dungeon[rn][c]
                if nc < costs[(rn,c)]:
                    costs[(rn,c)] = nc
                    heappush(heap,(nc,rn,c))
                
            if cn <= col:
                nc = cost - dungeon[r][cn]
                if nc < costs[(r,cn)]:
                    costs[(r,cn)] = nc
                    heappush(heap,(nc,r,cn))
        
        return ans
       
            
            