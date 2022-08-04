class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        @lru_cache(None)
        def gcd(p:int,q:int):
            if q==0:
                return p
            return  gcd(q,p%q)
    
        lcm = (p*q)/gcd(p,q)
                
        n = lcm //p
        m = lcm // q

        if n % 2 == 0:
            return 0
        
        if m % 2 == 0:
            return 2
        
        return 1
        
     

 