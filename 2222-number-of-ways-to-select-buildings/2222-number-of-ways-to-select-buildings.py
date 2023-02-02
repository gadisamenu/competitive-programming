class Solution:
    def numberOfWays(self, s: str) -> int:
        numbers = list(map(int,s))
        
        for  i in range(1,len(numbers)):
            numbers[i] += numbers[i-1]
            
        answer = 0
        
        for i in range(1,len(s)-1):
            if s[i] == "0":
                answer += numbers[i-1]*(numbers[-1] - numbers[i])
            else:
                answer += (i- numbers[i-1]) * ((len(s) - i- 1) - (numbers[-1]-numbers[i]))
                
        return answer
                
        
       