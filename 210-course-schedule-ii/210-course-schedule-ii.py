class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = deque()
        visited = set()
        graph = defaultdict(set)
        
        def dfs(course,path):
            visited.add(course)
            path.add(course)
            for nexts in graph[course]:
                if nexts in path:
                    return False
                if nexts not in visited:
                    if not dfs(nexts,path): return False
            ans.appendleft(course)
            path.remove(course)
            return True
            
        for course,pre in prerequisites:
            graph[pre].add(course)
    
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course,set()): return []
        return ans
                
        
            
  
            
        
        
        
        
        
        
        
        