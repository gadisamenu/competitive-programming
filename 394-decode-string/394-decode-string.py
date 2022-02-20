class Solution:
    def decodeString(self, s: str) -> str:
        return self.helper(s,s[0])
        
    
    def helper(self,s,m):
        i = 0
        t=None
        while i < len(s):
            if s[i] =="[":
                s = s[:t] + self.helper(s[i+1:],s[t:i])
                t=None
            elif s[i] == "]":
                return int(m)* s[:i] + s[i+1:]
            else:
                if s[i].isdigit() and t == None:
                    t=i
                    
                i +=1
                
        return s