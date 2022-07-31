class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0 
        negative = True if (dividend > 0 and  divisor < 0) or (dividend < 0 and divisor > 0)  else False
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        for i in range(31,-1,-1):
            if divisor << i  <= dividend:
                dividend -= divisor << i
                quotient += 1 << i
        
        if negative: quotient *= -1
        
            
        if quotient > 2147483647:
            return 2147483647
        if quotient < -2147483648:
            return -2147483648
        
        return quotient