class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1)])
        answer = 0
        while queue:
            lgth = len(queue)
            while lgth:
                position,speed = queue.popleft()
                if position == target:
                    return answer
                
                n_p = position + speed
                n_s = speed*2
                queue.append((n_p,n_s))
                
                if (n_p > target and speed > 0) or (n_p < target  and speed < 0):
                    speed = -1 if speed > 0 else 1
                    queue.append((position,speed))
                lgth -= 1
            answer += 1
    