class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        lgth = len(rolls) + n
        _sum = sum(rolls)
                
        missing = lgth* mean  - _sum
        if missing > 6*n or missing < 1*n:return  []
                   
        q = missing //n
        r = missing % n
        
        ans = []
        
        for i in range(n):
            if r:
                ans.append(q+1)
                r -= 1
            else:ans.append(q)
                
        return ans
        