class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
    
        def dfs(row):
            for i in range(len(isConnected[row])):
                if  isConnected[row][i] == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)
                    
        province =0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                province+=1

        return province
                
                
            
                    