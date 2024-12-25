class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        depth1,multipleCenter1 =  self.getMinHeight(edges1) 
        depth2,multipleCenter2= self.getMinHeight(edges2)
        
        existingMax = 0
        if depth1 > depth2:
            existingMax = depth1*2 + multipleCenter1
        elif depth1 < depth2:
            existingMax = depth2*2 + multipleCenter2
        else:
            existingMax = depth1*2 + multipleCenter1 if multipleCenter1 else multipleCenter2
            
        
        return max(depth1 + multipleCenter1 + depth2 + multipleCenter2 +1 , existingMax )
        
        
    def getMinHeight(self,edges) -> int:        
        visited = set()
        neighbours = defaultdict(set)
        queue = deque()
        
        for edge in edges:
            neighbours[edge[0]].add(edge[1])
            neighbours[edge[1]].add(edge[0])
     
        for node in neighbours:
            if len(neighbours[node]) == 1:
                visited.add(node)
                queue.append((node,0))
                
        layer_count = 0    
        answer = 0
        while queue:
            current,depth = queue.popleft()
            layer_count += 1
            if answer != depth:
                layer_count  = 1
                answer = depth

            for node in neighbours[current]:
                neighbours[node].remove(current)
                if node not in visited and len(neighbours[node]) == 1:
                    queue.append((node,depth +1))
                    visited.add(node)
                    
        multipleCenter = 1 if layer_count > 1 else 0
            
        return (answer,multipleCenter)
        
        