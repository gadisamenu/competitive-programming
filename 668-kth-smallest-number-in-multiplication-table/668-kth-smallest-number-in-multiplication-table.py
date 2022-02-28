class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def count(num):
            less_or_equals = 0
            for row in range(1,m+1):
                less_or_equals += min(num//row,n)
            
            return less_or_equals
            
                 
        
        left = 1
        right = m*n
        
        while left < right:
            try_num = left + (right-left)//2
            
            if count(try_num) < k:
                left = try_num + 1
            else:
                right = try_num
                
        return left
                
