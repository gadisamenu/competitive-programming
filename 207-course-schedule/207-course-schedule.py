class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(set)
        degrees = [0]*numCourses
        
        for p in prerequisites:
            graph[p[1]].add(p[0])
            degrees[p[0]]+=1
                        
        que  = deque()
        for course in range(numCourses):
            if not degrees[course]:
                que.append(course)
                                
        while que:
            cur_course = que.popleft()
            numCourses -=1
            for course in graph[cur_course]:
                degrees[course]-=1
                if not degrees[course]:
                    que.append(course)

        return False if numCourses else True
            