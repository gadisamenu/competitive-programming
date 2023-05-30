class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        self.answer = inf
        cookies.sort()
        
        groups = [0 for i in range(k)]
        
        def backtracking(index):
            if index >= len(cookies):
                self.answer = min(self.answer, max(groups))
                return
                
            for group in range(k):
                if groups[group] + cookies[index] < self.answer:
                    groups[group] += cookies[index]
                    backtracking(index+1)
                    groups[group] -= cookies[index]

    
        backtracking(0)
        return self.answer
 
                
                
            
            
