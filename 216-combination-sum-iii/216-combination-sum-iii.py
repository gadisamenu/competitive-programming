class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k or n > 45:return []
        if n == k: return [[1]*k]
        
        def recursion(i,sl,tgt):
            if sl == 0:
                if tgt == 0 :return [[]]
                return False
            if tgt < 0: return False
            ans = []
            for m in range(i+1,10):
                ret =  recursion(m,sl-1,tgt-m)
                if ret:
                    for a in ret:
                        a.append(m)
                        ans.append(a)
            return ans
        
        return recursion(0,k,n)
                        
                
            