class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
        _lcm = (divisor1*divisor2)/gcd(divisor1,divisor2)
        left = 1
        right = 2000000000
        
        
        while left < right:
            mdl = left + (right-left)//2
            not_1 = mdl//divisor1
            not_2 = mdl//divisor2
            not_both = mdl//_lcm
    
            
            if mdl- not_both < uniqueCnt1 + uniqueCnt2 or mdl- not_1 < uniqueCnt1 or mdl-not_2 < uniqueCnt2:
                left = mdl+1
            else:
                right = mdl
  
        return right
