class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lgth = len(matrix)-1
        i,j = 0,0
        
        while lgth>-1:
            for n in range(lgth):
                matrix[i][j+n],matrix[i+n][j+lgth],matrix[i+lgth][j+lgth-n],matrix[i+lgth-n][j]= matrix[i+lgth-n][j],matrix[i][j+n],matrix[i+n][j+lgth],matrix[i+lgth][j+lgth-n]
            lgth -= 2 
            i+=1
            j+=1
            
            