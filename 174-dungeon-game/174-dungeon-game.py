class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon)-1
        col = len(dungeon[0])-1
        
        dp = deque()
        sm = 0
        for i in range(col,-1,-1):
            sm += dungeon[-1][i]
            dp.appendleft(sm)
            if sm > 0:sm = 0
                
        for r in range(row-1,-1,-1):
            for c in range(col,-1,-1):
                if c == col:
                    if dp[c] < 0: dp[c] += dungeon[r][c]
                    else: dp[c] = dungeon[r][c]
                else:
                    m = max(dp[c],dp[c+1])
                    if m < 0: dp[c]= m + dungeon[r][c]
                    else:dp[c] = dungeon[r][c]
                        
        return abs(dp[0])+1 if dp[0] < 0 else 1
                
                
       
    
            
            