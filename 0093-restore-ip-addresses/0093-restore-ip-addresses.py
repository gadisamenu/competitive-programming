class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answer=[]
        path=[]
        def backtrack(i):
            if i==len(s) and len(path)==4:
                answer.append(".".join(path))
                return
            if len(path)>4 or i>=len(s):
                return
            
            if s[i]=='0':
                path.append(s[i])
                backtrack(i+1)
                path.pop()
                return
            
            j=0
            while j<4 and i+j<len(s):
                if int(s[i:i+j+1])<256:
                    path.append(s[i:i+j+1])
                    backtrack(i+j+1)
                    path.pop()
                j+=1
                
        backtrack(0)
        return answer
        
            
            
        