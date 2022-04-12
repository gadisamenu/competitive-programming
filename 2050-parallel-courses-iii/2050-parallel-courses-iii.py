class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(set)
        incoming = [0 for x in range(n)]
        end_time = defaultdict(int)
        max_time = defaultdict(int)
        que = deque()
        
        for pre,nex in relations:
            graph[pre].add(nex)
            incoming[nex-1]+=1
            
        for course in range(n):
            if incoming[course]== 0:
                que.append(course+1)
                
        while que:
            course = que.popleft()
            end_time[course] = max_time[course]+time[course-1]
            for nex in graph[course]:
                incoming[nex-1]-=1
                if max_time[nex] < end_time[course]:max_time[nex]= end_time[course]
                if not incoming[nex-1]:
                    que.append(nex)
    
        return max(end_time.values())
        