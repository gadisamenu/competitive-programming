class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        
        self.data = Counter(nums)
        self.ans =  0
        def dfs(pre):
            if not self.data: self.ans += 1
            else:
                keys = list(self.data.keys())
                for key in keys:
                    rt = sqrt(key+pre)
                    if rt == int(rt):
                        if self.data[key] > 1: self.data[key] -=1
                        else: self.data.pop(key)
                        dfs(key)
                        self.data[key] += 1
    
        keys = list(self.data.keys())
        for n in  keys:
            if self.data[n] > 1: self.data[n] -=1
            else: self.data.pop(n)
            dfs(n)
            self.data[n] += 1
            
        
        return self.ans