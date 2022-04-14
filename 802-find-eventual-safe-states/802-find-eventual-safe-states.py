class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rotating_members = set()
        path = set()      
        ans =[]
        
        @lru_cache(None)
        def top(ind):
            if not graph[ind]:
                return True
            state = True
            path.add(ind)
            for _next in graph[ind]:
                if _next in path:
                    rotating_members.update(path)
                    state = False
                elif _next in rotating_members:
                    rotating_members.add(ind)
                    state = False
                else:
                    state = state and top(_next)
                    
            if ind in path: path.remove(ind)
            if state:
                return True
            rotating_members.add(ind)
            return False
        
        
        for node in range(len(graph)):
            top(node)
        for node in range(len(graph)):
            if node not in rotating_members:
                ans.append(node)
        return ans
                    



                
        
        