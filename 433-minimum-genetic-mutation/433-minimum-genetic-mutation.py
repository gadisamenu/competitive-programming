class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited= set()
        queue = deque([(start,0)])
        while queue:
            word,lv = queue.popleft()
            visited.add(word)
            if word == end:
                return lv
            for w in bank:
                if w not in visited:
                    
                    dif = 0
                    for i in range(len(start)):
                        if word[i] !=  w[i]:
                            dif += 1
                    if dif == 1:
                        queue.append((w,lv+1))
        return -1
                    

            