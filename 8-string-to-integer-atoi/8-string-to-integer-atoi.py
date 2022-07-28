class Solution:
    def myAtoi(self, s: str) -> int:
        
        digits = {'1','2','3','4','5','6','7','8','9','0'}
        integer = 0
        
        started = False
        n_digits = 0
        negative = False
        
        for ch in s:
            if not started:
                if ch == ' ':
                    continue
                
                elif ch == '-':
                    negative = True
                    started = True
                    continue
                    
                elif ch in ['+']:
                    started = True
                    continue
                    
            if ch  in digits:
                started = True
                n_digits+= 1
                integer += (int(ch)/10**n_digits)
            
            else: break
                
        integer = int(round(integer * 10 ** n_digits,0))
                    
        if negative:
            integer *= -1
            
        _min = pow(-2,31)
        if integer < _min:
            return _min
        elif integer > (-1*(_min +1)):
            return (-1*(_min + 1))
        return integer
                
                    
            
                    
                
        
        
        
        