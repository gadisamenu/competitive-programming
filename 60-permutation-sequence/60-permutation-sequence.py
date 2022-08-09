from itertools import permutations 
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perm = list(permutations([x for x in range(1,n+1)]))
        return "".join(map(str,perm[k-1]))
        
        
        
        
