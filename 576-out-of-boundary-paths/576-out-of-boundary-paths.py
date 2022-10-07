class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.ans = 0
        out_of_bound = lambda r,c: r < 0 or r >= m or c < 0 or c >= n
        DIR = [0,1,0,-1,0]
        
        @cache
        def dp(moves,r,c):
            if out_of_bound(r,c): return 1
            ans = 0
            if moves:
                for i in range(4):
                    ans += dp(moves-1,r+DIR[i],c+DIR[i+1])
                    
            return ans
                              
        return dp(maxMove,startRow,startColumn)%1000000007