class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            m = left + (right -left)//2
            
            if m*m < x:
                candidate = m
                left = m+1
            elif m*m > x:
                right= m-1
            else:
                return m
        return candidate
            
            
                
        