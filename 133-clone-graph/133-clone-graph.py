"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        pairing = {}
       
        def dfs(root):
            if root:
                if root.val in pairing:
                    return pairing[root.val]
                
                new = Node(root.val,[])
                pairing[root.val] = new
                for n in root.neighbors:
                    new.neighbors.append(dfs(n)) 
                return new
                        
    
        return dfs(node)
            