class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        reds = defaultdict(list)
        blues = defaultdict(list)
        
        for edge in redEdges:
            reds[edge[0]].append(edge[1])
            
        for edge in blueEdges:
            blues[edge[0]].append(edge[1])
            
        anr = [-1 for i in range(n)]
        que = [(0,0)]
        ans = 0
        visited = set([(0,0)])
        while que:
            lvl = set()
            while que:
                n,c = que.pop()
                if anr[n] == -1: anr[n] = ans
                if c != 1:
                    for m in reds[n]:
                        if (m,1) not in visited: lvl.add((m,1))
                if c != 2:
                    for m in blues[n]:
                        if (m,2) not in visited: lvl.add((m,2))         
            ans += 1
            visited.update(lvl)
            que = lvl
        return anr
                    
            
            