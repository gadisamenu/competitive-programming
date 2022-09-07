class Solution:
    def isNumber(self, s: str) -> bool:
        dot= 1
        e = None
        num = 0
        if len(s) == 1:
            return True if s[0].isdigit() else False
        
        for ind in range(len(s)):
            if s[ind] == "E" or s[ind] == "e":
                if e == None and (num):
                    e = ind
                    num = 0
                else: return False
            
            elif s[ind] in {"+","-"}:
                if ind != 0 and e != ind -1: return False
                    
            elif s[ind] == ".":
                if dot and e==None: dot -= 1
                else: return False
                
            elif s[ind].isdigit():
                num +=1 
                
            else:return False
            
        if (((e != None and num) or (e == None))and (dot or num)): return  True
        return False
    
