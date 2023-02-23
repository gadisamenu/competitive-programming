class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if rows < 3 or cols < 3 :
            return 0
        
        rows -= 2
        cols -= 2
        magic_squares = 0
        
        for  r in range(rows):
            for c in range(cols):
                if self.check(r,c,grid):
                    magic_squares += 1
                    
        return magic_squares
    
    def check(self,row,col,grid):
        rows_sum = [0,0,0]
        cols_sum = [0,0,0]
        numbers = set(range(1,10))

        for r in range(row,row+3):
            for c in range(col,col+3):
                if grid[r][c] in numbers:
                    numbers.remove(grid[r][c])
                else:
                    return False
                rows_sum[r-row] += grid[r][c]
                cols_sum[c-col] += grid[r][c]
                
        if rows_sum[0] == rows_sum[1] == rows_sum[2]:
            if cols_sum[0] == cols_sum[1] == cols_sum[2]:
                diagonal = 0
                for i in range(3):
                    diagonal += grid[row][col]
                    row += 1
                    col += 1
                    
                ant_diagonal = 0
                
                col -= 3
                row -= 1
                for i in range(3):
                    ant_diagonal += grid[row][col]
                    row -= 1
                    col += 1
                    
                if diagonal == ant_diagonal == rows_sum[0]:
                    return True
             
        return False
    