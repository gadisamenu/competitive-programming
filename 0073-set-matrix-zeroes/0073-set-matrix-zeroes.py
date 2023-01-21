class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        row = set()
        col = set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)

        for r in row:
            for c in range(cols):
                matrix[r][c] = 0
        
        for c in col:
            for r in range(rows):
                matrix[r][c] = 0