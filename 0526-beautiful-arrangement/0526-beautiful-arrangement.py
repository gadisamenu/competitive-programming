class Solution:
    def countArrangement(self, n: int) -> int:
        n+=1
        @cache
        def dp(index,visited):
            if index == n:
                return 1
            answer = 0
            
            for  num  in range(1,n):
                if (visited &1 <<  num ) == 0 and (index% num  == 0 or  num %index == 0):
                    answer += dp(index + 1,visited | 1 << num)
                    
            return answer
                            
        return dp(1,0)
            
            
            