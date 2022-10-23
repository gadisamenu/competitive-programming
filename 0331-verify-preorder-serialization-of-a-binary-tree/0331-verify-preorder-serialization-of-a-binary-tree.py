class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        def dfs(i):
            if i >= len(preorder): return i,False
            if preorder[i] == "#": return i+2,True
            while i < len(preorder) and preorder[i] !=",":
                i += 1
            i,valid = dfs(i+1)
            if not valid: return i,False
            i,valid = dfs(i)
            return i,valid
        
        i,valid = dfs(0)
        
        return True if i >= len(preorder) and valid else False