class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(s_ind:int,p_ind:int)-> bool:
            if  s_ind == len(s):
                return True if p_ind == len(p) or ((len(p) - p_ind)%2 == 0 and "*"*((len(p) - p_ind )//2)  ==  "".join([x if ind%2 == 1 else "" for ind, x in enumerate(p[p_ind:])])) else False
            
            if p_ind == len(p):  return False
            
            special = p[p_ind] if(p_ind + 1 < len(p) and p[p_ind+1] == "*") else False
            
            if special:
                ans = False
                if special == s[s_ind] or special == ".": ans |= dp(s_ind+1,p_ind)
                if not ans: ans |= dp(s_ind,p_ind+2)
                return ans 
            
            if s[s_ind] == p[p_ind] or p[p_ind] == ".":
                return dp(s_ind+1,p_ind+1)
            
            return False
            
                
                
        return dp(0,0)
