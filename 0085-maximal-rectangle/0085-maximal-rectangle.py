class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        answer = 0
        dp = [[ 0 for _ in range(cols+1)] for _ in range(rows)]
        
        
        for row in range(rows- 1,-1,-1):
            for col in range(cols-1,-1,-1):
                if matrix[row][col] == "1":
                    dp[row][col] = dp[row][col+1] + 1
                    width = dp[row][col]
                    for w in range(row,rows):
                        if not dp[w][col]:
                            break
                        width = min(dp[w][col],width)
                        answer = max(answer,width * (w - row + 1))
                        
                else:
                    dp[row][col] = 0
    
        return answer
        

