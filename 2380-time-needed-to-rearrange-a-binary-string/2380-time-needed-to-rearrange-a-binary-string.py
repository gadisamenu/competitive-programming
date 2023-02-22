class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        count = 0
        change = True
        
        while change:
            change = False
            i = 0
            while i < len(s)-1:
                if s[i] == "0" and s[i+1] =="1":
                    s[i] ="1" 
                    s[i+1] = "0"
                    change = True
                    i+= 1
                i+= 1
            if change : count+= 1
                
        return count