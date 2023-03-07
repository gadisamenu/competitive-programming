class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2,1),(-2,-1),(2,1),(2,-1),(1,-2),(-1,-2),(1,2),(-1,2)]
        
        in_bound = lambda r,c: -1 < r< n and -1 < c < n
        
        @cache
        def dp(row,col,k):
            answer =  0
            if not k:
                return 1
            k -= 1
            for move in moves:
                n_row = row + move[0]
                n_col = col + move[1]
                if in_bound(n_row,n_col):
                    answer += dp(n_row,n_col,k)

            return answer
        
        return dp(row,column,k)/(8**k)