class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(idx):
            array = matrix[idx]
            left = 0
            right = len(array) - 1
            
            while left <= right:
                
                md = left + (right - left)// 2
                
                md_val = array[md]
                
                if md_val == target:
                    return True
                
                elif md_val < target:
                    left = md + 1
                else:
                    right = md -1
            return False
                
        ans  = False
        
        for idx in range(len(matrix)):
            ans |= binary_search(idx)
            
        
        return ans
            

