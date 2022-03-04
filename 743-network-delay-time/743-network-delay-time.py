class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {}
        for t in times:
            if t[0] in edges:
                edges[t[0]][t[1]]=t[2]
            else:
                edges[t[0]] ={t[1]:t[2]}

        heap  = []
        heappush(heap,(0,k))
        visited = set()
        while heap:
            cr = heappop(heap)
            if cr[1] in visited:
                continue
            visited.add(cr[1])
            if cr[1] in edges:
                for e in edges[cr[1]]:
                    if e not in visited:
                        heappush(heap,(cr[0]+edges[cr[1]][e],e))
                edges.pop(cr[1])
            ans = cr[0]
        
        return ans if len(visited) == n  else -1
 