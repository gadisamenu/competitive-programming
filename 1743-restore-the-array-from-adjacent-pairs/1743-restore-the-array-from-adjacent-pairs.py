class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for pair in adjacentPairs:
            in_degree[pair[0]] += 1
            in_degree[pair[1]] += 1
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
      
        for num in in_degree:
            if in_degree[num] == 1:
                start = num
    
        
        lgth = len(adjacentPairs)
        
        answer = [start]
        for i in range(lgth):
            _nxt = graph[start][0]
            graph[_nxt].remove(start)
            start = _nxt
            answer.append(start)
            
        return answer
            