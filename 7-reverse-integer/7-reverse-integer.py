class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            reverse = int(str(x)[::-1])
            limit= 2147483647
            return reverse if (reverse % limit) ==  reverse else 0
        
        reverse2 = int(str(x)[:0:-1])
        limit2 = 2147483648
        
        return reverse2 *-1 if  (reverse2 % limit2) == reverse2 else 0
        
        
    
    
        