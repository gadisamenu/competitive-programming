class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k != 1:
            return "".join(sorted(s))
        answer = s
        queue = deque(s)
       
        for i in range(len(s)):
            queue.append(queue.popleft())
            for j in range(len(s)):
                if answer[j] != queue[j]:
                    if answer[j] > queue[j]:
                        answer = list(queue)
                    break
                
        return "".join(answer)
        
            
        