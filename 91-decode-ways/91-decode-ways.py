class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        
        self.valid= True
        @cache
        def recur(ind):
            if ind <= 0: return 1
            
            if s[ind] == "0":
                if s[ind-1] == "2"or s[ind-1]== "1":
                    return recur(ind-2)
                self.valid = False
                return 0
                
        
            if ind -1 >= 0:
                if s[ind-1] == "1" or (s[ind - 1] == "2" and s[ind] < "7"):
                    return recur(ind -1) + recur(ind - 2)
               
            return recur(ind -1)
            
            
        ans = recur(len(s)-1)
        
        return ans  if self.valid  else 0
    
    
