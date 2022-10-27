class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        for edge in edges:
            if self.merge(edge[0],edge[1],parent):
                return edge

    def find(self,nd,parent):
        if nd == parent[nd]:
            return nd
        parent[nd] = self.find(parent[nd],parent)
        return parent[nd]
    
    def merge(self,first,second,parent):
        parent1 = self.find(first,parent)
        parent2 = self.find(second,parent)
        parent
        if parent2 == parent1:
            return True
        parent[parent1] = parent2
        return False

   

            
        
            