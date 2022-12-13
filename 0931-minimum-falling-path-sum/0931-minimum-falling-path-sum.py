class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        get_value = lambda r,c: matrix[r][c] if -1 < r < rows and -1 < c < cols else float("inf")
        
        for r in range(1,rows):
            for c in range(cols):
                matrix[r][c] += min(get_value(r-1,c),get_value(r-1,c+1),get_value(r-1,c-1))
      
        return min(matrix[-1])
        

            