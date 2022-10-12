class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group= {1:set(),2:set()}
        visited = set()
        
        def dfs(nd,c):
            ans = True
            nxt_c = 2 if c == 1 else 1   
              
            group[c].add(nd)                
            for _nxt in graph[nd]:
                if _nxt not in visited:
                    visited.add(_nxt)
                    ans &= dfs(_nxt,nxt_c)
                else:
                    if _nxt in group[c]:
                        return False
            return ans
                            
        
        for i in range(len(graph)):
            if i not in visited:
                visited.add(i)
                if not dfs(i,1):return False
            
        return True