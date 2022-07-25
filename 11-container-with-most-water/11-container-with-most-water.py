class Solution:
    def maxArea(self, height: List[int]) -> int:
        shorter = lambda i,j: True if height[i] < height[j] else False
        area = 0
        i = 0
        j = len(height) - 1
        
        while i < j:
            cur_area = (j-i) * min(height[i], height[j])
            area = max(area,cur_area) 
            if shorter(i, j):
                _min = height[i]
                while height[i] <= _min and i < j:
                    i += 1
            else:
                _min = height[j]
                while height[j] <= _min and i < j:
                    j -= 1
            
        return area
                
                    