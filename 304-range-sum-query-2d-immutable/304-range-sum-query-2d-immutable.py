class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row = len(matrix)
        self.col = len(matrix[0])
        get = lambda r,c: matrix[r][c] if -1 < r < self.row and -1 < c < self.col else 0
        for i in range(self.row):
            for j in range(self.col):
                matrix[i][j] = matrix[i][j] + get(i-1,j) + get(i,j-1) -get(i-1,j-1)
        
        self.prefix_2d = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        get = lambda r,c: self.prefix_2d[r][c] if -1 < r < self.row and -1 < c < self.col else 0
        return get(row2,col2) - get(row1-1,col2) - get(row2,col1-1) + get(row1-1,col1-1)
    
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)