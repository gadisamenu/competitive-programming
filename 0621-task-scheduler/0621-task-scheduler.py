class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        
        heap = [(-task_count[task],task) for task in task_count]
        
        heapify(heap)
        queue = deque()
        
        time = 0
        taskCount = len(tasks)
        
        while taskCount > 0:
            if len(queue) > n:
                task = queue.popleft()
                if task:
                    heappush(heap,task)
    
            if heap:
                count,task = heappop(heap)
                if count < -1:
                    queue.append((count + 1,task ))
                else:queue.append(None)
                taskCount -= 1
            else:
                queue.append(None)
          
            time += 1
    
        return time
            
                
                
            
            
             
        
        
        
        
        
   
        
        
        
        
        
        return 0