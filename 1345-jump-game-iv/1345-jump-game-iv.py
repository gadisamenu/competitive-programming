class Solution:
    def minJumps(self, arr: List[int]) -> int:
        lgth = len(arr)
        isValid = lambda ind: -1<ind<lgth
        
        positions = defaultdict(set)
        # graph = defaultdict(set)
        
        i = 0
        j = 0
        while j < lgth:
            if arr[i] == arr[j]:
                j +=1
            else:
                positions[arr[i]].add(i)
                positions[arr[i]].add(j-1)
                i = j
        positions[arr[i]].add(j-1)
        
        
        que = deque([(0,0)])
        visited = {0}
        while que:
            cur = que.popleft()
            if cur[0] == lgth -1:
                return cur[1]
            
            if isValid(cur[0]+1) and cur[0]+1 not in visited:
                visited.add(cur[0]+1)
                que.append((cur[0]+1,cur[1]+1))
            if isValid(cur[0]-1) and cur[0]-1 not in visited:
                visited.add(cur[0]-1)
                que.append((cur[0]-1,cur[1]+1))
            
            for nb in positions[arr[cur[0]]]:
                if nb not in visited:
                    visited.add(nb)
                    que.append((nb,cur[1]+1))
            positions.pop(arr[cur[0]])
        