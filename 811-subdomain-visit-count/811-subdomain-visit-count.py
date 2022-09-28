class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        visit_count = defaultdict(int)
        for cpd in cpdomains:
            val,domain = cpd.split()
            val = int(val)
            
            visit_count[domain] += val
            for ind in range(len(domain)):
                if domain[ind] == ".":
                    visit_count[domain[ind+1:]]+=val
                    
        return list(map(lambda x: str(visit_count[x])+ " " + x, visit_count))
                    
                
            