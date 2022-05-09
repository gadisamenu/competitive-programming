class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        
        for p in path:
            if p == "..":
                if stack: stack.pop()
            elif p  == "." or p == "":
                pass
            else:
                stack.append(p)
        return "/"+"/".join(stack)
            
                
            
            