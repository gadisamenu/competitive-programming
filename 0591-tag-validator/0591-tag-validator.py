class Solution:
    def isValid(self, code: str) -> bool:
                
        isUpper = lambda x: 65 <= ord(x) <= 90
        
        CDATA = "[CDATA["    
        CDATA_E = "]]>"
        
        inCDATA = False
        stack = []
        validStart = False
        
        openTag = False
        closeTag = False
        
        
        start = 0
        end = 0
        
        while end < len(code):
            if openTag:
                if isUpper(code[end]):
                    end += 1
                elif code[end] == ">":
                    if (not stack and start != 0):
                        return False
                    
                    lgth = end -start
                    
                    if lgth < 2 or lgth > 11 or ((not closeTag) and lgth > 10):
                        return False
                    
                    if closeTag:
                        if not stack or stack[-1] != code[start+2:end]: 
                            return False
                        stack.pop()
                        closeTag = False
                    else: 
                        validStart = True
                        stack.append(code[start+1:end])
                    openTag = False
                    end += 1
                
                    
                elif code[end] == "/":
                    if end-start != 1 or not stack:
                        return False
                    closeTag = True
                    end += 1
                    
                elif code[end] == "!":
                    if end-start != 1 or CDATA != code[end+1:end + len(CDATA)+1] or not stack:
                        return False
                    inCDATA = True
                    end += len(CDATA) + 1
                    openTag = False
                    closeTag = False
                    
                else: return False
                    
            elif inCDATA:
                if code[end:end+len(CDATA_E)] == CDATA_E:
                    inCDATA = False
                    end += len(CDATA_E) -1
                end += 1
                    
            elif code[end] == "<":
                start = end
                openTag = True
                end += 1
                
            elif not stack: 
                return False
            
            else: end += 1
            
        
        return False if (stack or inCDATA or openTag or not validStart or closeTag) else True
  
            
