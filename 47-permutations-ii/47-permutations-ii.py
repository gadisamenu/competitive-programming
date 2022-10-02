class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.data = Counter(nums)
        
        self.ans = []
        def dfs():
            if not self.data:
                self.ans.append([])
                return [len(self.ans)-1]
            
            keys = list(self.data.keys())
            
            inds = []
            for key in keys:
                if self.data[key] > 1: self.data[key] -=1
                else: self.data.pop(key)
                    
                ret = dfs()
                self.data[key] += 1
                
                inds += ret
                for ind in ret:
                    self.ans[ind].append(key)
                    
            return inds
        
        dfs()
        return self.ans
            
                    
                    