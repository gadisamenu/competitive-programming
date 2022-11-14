class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
                
        graph_col = defaultdict(list)
        graph_row = defaultdict(list)
        
        for i in range(len(stones)):
            stones[i] = tuple(stones[i])
            graph_row[stones[i][0]].append(stones[i])
            graph_col[stones[i][1]].append(stones[i])
     
        def bfs(stone,visited):
            answer = 0
            visited.add(stone)
            queue = deque([stone])
            while queue:
                stone = queue.popleft()
                for next_stone in graph_row[stone[0]]:
                    if next_stone not in visited:
                        answer += 1
                        queue.append(next_stone)
                        visited.add(next_stone)
                for next_stone in graph_col[stone[1]]:
                    if next_stone not in visited:
                        answer += 1
                        queue.append(next_stone)
                        visited.add(next_stone)
                        
            return answer
        
        answer = 0
        visited = set()
        for stone in stones:
            if stone not in visited:
                answer += bfs(stone,visited)
                
        return answer
            
            
        
