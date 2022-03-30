class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2== 1: return False
        openning = 0 
        flipable= 0
        for ind in range(len(s)):
            if locked[ind]== "0":
                flipable+=1
            elif s[ind] == ")":
                if openning:openning-=1
                elif flipable: flipable-=1
                else: return False
            else:
                openning+=1
        openning=flipable=0
        for ind in range(len(s)-1,-1,-1):
            if locked[ind]== "0":
                flipable+=1
            elif s[ind] == "(":
                if openning:
                    openning-=1
                elif flipable: flipable-=1
                else: return False
            else:
                openning+=1
        return True
        
    