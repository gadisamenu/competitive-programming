class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        for row in grid:
            left = 0
            right = len(row)-1
            
            while left <= right:
                m = left + (right-left)//2
                
                if row[m] < 0:
                    right = m-1
                else:
                    left = m + 1
           
            negatives += len(row)-max(left,right)
            
        return negatives