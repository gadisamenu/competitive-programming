class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda:{})
        
        for i in range(len(equations)):
            eqn = equations[i]
            graph[eqn[0]][eqn[1]] = values[i]
            graph[eqn[1]][eqn[0]] = (1/values[i])
      
        answer = []
        for query in queries:
            if query[0] == query[1]:
                if query[0] in graph:
                    answer.append(1)
                else:
                    answer.append(-1)
            else:
                answer.append(self.bfs(query[0],query[1],graph))
                
        return answer
        
    def bfs(self,start,end,graph):
        visited = set([start])
        queue = deque([(start,1)])
        while queue:
            var, value = queue.popleft()
            if var == end:
                return value
            for _nxt in graph[var]:
                if _nxt not in visited:
                    queue.append((_nxt,value * graph[var][_nxt]))
                    visited.add(_nxt)
        
        return -1
        
        
            