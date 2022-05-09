class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        graph = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        path = []
        ans  = []
           
        
        def dfs(idx):
            if idx == len(digits):
                ans.append("".join(path))
                return 

            for char in graph[digits[idx]]:
                path.append(char)
                dfs(idx+1)
                path.pop()
            
        dfs(0)
        return ans