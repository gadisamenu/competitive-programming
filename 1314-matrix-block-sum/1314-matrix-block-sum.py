class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
    
        self.prefix(mat)
     
        answer = []        
        for i in range(rows):
            answer.append([])
            for j in range(cols):
                answer[-1].append(self.get_sum(i,j,k,mat))
                
        return answer
    
    def get_sum(self,r,c,k,matrix):
        start_r,end_r = max(r-k,0),min(r+k,len(matrix)-1)
        start_c,end_c = max(c-k,0),min(c+k,len(matrix[0])-1)
        
        answer = matrix[end_r][end_c]
        if start_r > 0:
            if start_c > 0:
                answer += matrix[start_r-1][start_c-1] - matrix[end_r][start_c-1]
            answer -= matrix[start_r-1][end_c]
            
        elif start_c > 0:
            answer -= matrix[end_r][start_c - 1]
        
        return answer        
        
    
    def prefix(self,matrix):
        for c in range(1,len(matrix[0])):
            matrix[0][c]+= matrix[0][c-1]
        for r in range(1,len(matrix)):
            matrix[r][0]+= matrix[r-1][0]
        
        for  r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                matrix[r][c] +=  matrix[r-1][c] + matrix[r][c-1] - matrix[r-1][c-1]
                
        
        
            
            
        