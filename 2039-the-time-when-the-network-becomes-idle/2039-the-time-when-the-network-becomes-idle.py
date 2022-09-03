class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(list)
        lgth = len(patience)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        min_cost = [-1 for _ in range(lgth)]
        visited = {0}
        queue = deque([(0,0)])
        
        while queue:
            cur,cst = queue.popleft()
            min_cost[cur] = cst
            
            for ngh in graph[cur]:
                if ngh not in visited:
                    visited.add(ngh)
                    queue.append((ngh,cst+1))
     
    
        ans = 0
        for i in range(1,lgth):
            t = 2*min_cost[i]
            t = t //patience[i] if t %patience[i] else t //patience[i] -1
            time = t* patience[i] + 2*min_cost[i]
            ans = max(ans,time)
        return ans + 1
            

        