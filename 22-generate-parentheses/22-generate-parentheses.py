class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
              
        def dp(opened = 0, closed= 0):
            if opened == n and closed == n:
                return [deque()]
                
            result = []
            if opened < n:
                first = dp(opened+1,closed)
                for ans in first:
                    ans.appendleft('(')
                    result.append(ans)
                
            if opened and opened > closed:
                second = dp(opened,closed+1)
                for ans in second:
                    ans.appendleft(')')
                    result.append(ans)
                    
            return result
        
                
        parentheses = dp()
        
        for ind in range(len(parentheses)):
            parentheses[ind] = ''.join(parentheses[ind])
        
        return parentheses
            
                    
                    
                    
            
            