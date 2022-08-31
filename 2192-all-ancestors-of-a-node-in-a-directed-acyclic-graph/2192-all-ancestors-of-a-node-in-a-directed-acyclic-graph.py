class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        in_degrees = defaultdict(int)
        graph = defaultdict(list)
        ans = [set() for _ in range(n)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            in_degrees[edge[1]]+= 1                                               
            
        queue = deque()
        for _ in range(n):
            if not in_degrees[_]:
                queue.append(_)
   
        while queue:
            node = queue.popleft()
            for ngh in graph[node]:
                in_degrees[ngh] -= 1
                ans[ngh].add(node)
                ans[ngh].update(ans[node])
                if not in_degrees[ngh]:
                    queue.append(ngh)
                    
        for ind in range(len(ans)):
            ans[ind]=sorted(ans[ind])
        return ans            
            
        