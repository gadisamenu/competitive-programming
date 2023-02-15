class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dp(index,openning):
            if index >= len(s):
                return True if not openning else False
            if openning < 0:
                return False
        
            if s[index] == "(":
                return dp(index + 1,openning+1)
                
            if s[index] == ")":
                return dp(index + 1,openning-1)
        
            return dp(index + 1,openning+1) or dp(index + 1,openning-1) or  dp(index + 1,openning)
        
        return dp(0,0)
        

                
            
    