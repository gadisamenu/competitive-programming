class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        row = len(matrix)
        col = len(matrix[0])
        
        start = 0
        end= (row*col)-1
                
        while start <= end:
            
            mdl = start + (end - start)//2
            
            r_ind = (mdl//col)
            c_ind = (mdl% col)
            
            if matrix[r_ind][c_ind] < target:
                start = mdl + 1
                
            elif matrix[r_ind][c_ind] > target:
                end = mdl - 1
            else:
                return True
            
        return False
            
     