class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = {}
        for ltr in string.ascii_lowercase:
            parent[ltr] = ltr
        
        for i in range(len(s1)):
            self.merge(s1[i],s2[i],parent)
            
        answer = []
        for i in range(len(baseStr)):
            answer.append(self.find(baseStr[i],parent))
        
        return "".join(answer)
        
    
    def find(self,ltr,parent):
        if ltr == parent[ltr]:
            return ltr
        parent[ltr] = self.find(parent[ltr],parent)
        return parent[ltr]
        
    def merge(self,ltr1,ltr2,parent):
        parent1 = self.find(ltr1,parent)
        parent2 = self.find(ltr2,parent)
        
        if parent1 != parent2:
            if parent1 > parent2:
                parent2,parent1 = parent1,parent2
            parent[parent2]=parent1
        