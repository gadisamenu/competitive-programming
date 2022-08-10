class Solution:
    def isMatch(self, s: str, p: str) -> bool:        
        @cache
        def dp(s_ind:int,p_ind:int,star=False)-> bool:
            if  s_ind == len(s):
                return True if p_ind == len(p) or "*"*(len(p) - p_ind) == p[p_ind:] else False
             
            if p_ind == len(p): return False
            
            if star:
                return dp(s_ind+1,p_ind+1) or dp(s_ind +1,p_ind,True) or  dp(s_ind,p_ind+1)

            if s[s_ind] == p[p_ind] or p[p_ind] == "?":
                return dp(s_ind+1,p_ind+1)
            
            if p[p_ind] == "*":
                return dp(s_ind+1,p_ind,True) or  dp(s_ind,p_ind+1) or dp(s_ind+1,p_ind +1)
                
            
        return dp(0,0)
    