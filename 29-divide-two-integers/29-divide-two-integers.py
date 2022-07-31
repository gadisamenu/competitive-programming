class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        
        
        negative = True if (dividend > 0 and  divisor < 0) or (dividend < 0 and divisor > 0)  else False
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0 
        for i in range(31,-1,-1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                quotient += 1 << i
        
        
        return quotient * -1 if negative else quotient