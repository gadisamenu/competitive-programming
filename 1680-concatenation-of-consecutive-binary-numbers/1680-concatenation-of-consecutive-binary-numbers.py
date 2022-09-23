class Solution:
    def concatenatedBinary(self, n: int) -> int:        
        return int("".join(map(lambda x:bin(x).replace("0b",""),range(1,n+1))),2)%1000000007
            
            