class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        my_pre=defaultdict(set)
            
        for p in prerequisites:
            my_pre[p[0]].add(p[1])
            
        que  = deque()
        for num in range(numCourses):
            if not my_pre[num]:
                que.append(num)
                                
        while que:
            cur = que.popleft()
            numCourses -=1
            for course in my_pre:
                if cur in my_pre[course]:
                    my_pre[course].remove(cur)
                    if not my_pre[course]:
                        que.append(course)
                            
        return False if numCourses else True
            