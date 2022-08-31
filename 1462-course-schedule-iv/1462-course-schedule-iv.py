class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        in_degrees = defaultdict(int)
        graph = defaultdict(list)
        ans = [set() for _ in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
            in_degrees[prerequisite[1]]+= 1                                               
            
        queue = deque()
        for _ in range(numCourses):
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
                    
        ret = []
        for query in queries:
            ret.append(True) if query[0] in ans[query[1]] else ret.append(False)
        return ret