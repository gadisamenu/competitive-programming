class Solution:
    def compress(self, chars: List[str]) -> int:
        times = 0
        pre = None
        writer = 0
        for char in chars:
            
            if char == pre or not pre:
                times+=1
                pre = char
            else:
                writer = self.updateChars(chars,pre,times,writer)                    
                pre = char
                times= 1
                
        writer= self.updateChars(chars,pre,times,writer)   
        
        del chars[writer:] 
                
        return len(chars)
                
        
        
    def updateChars(self,chars,pre,times,n):
        if times > 1:
            chars[n] =pre
            times = str(times)
            for t in times:
                n+=1
                chars[n] =t
            n+=1
        else:
            chars[n] = pre
            n+=1
        return n
