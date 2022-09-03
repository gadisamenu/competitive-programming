class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        stack = [ (x,[str(x)]) for x in range(1,10)]
        ans = set()
        
        while stack:
            val,path = stack.pop()
            if len(path) == n:
                ans.add(int("".join(path)))
                continue
            if val + k  < 10:
                p = path[::]
                p.append(str(val+k))
                stack.append((val+k,p))
            if val -k > -1:
                p = path[::]
                p.append(str(val-k))
                stack.append((val-k,p))
    
        return ans
            
            